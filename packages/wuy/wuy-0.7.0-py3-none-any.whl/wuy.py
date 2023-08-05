# -*- coding: utf-8 -*-
# #############################################################################
#    Copyright (C) 2018 manatlan manatlan[at]gmail(dot)com
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 2 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# https://github.com/manatlan/wuy
# #############################################################################

from aiohttp import web
import aiohttp
import asyncio
import json,sys,os
import webbrowser
import traceback
import uuid
import inspect
import types
import base64
import socket
import tempfile
from threading import Thread

__version__="0.7.0"

DEFAULT_PORT=8080

application=None
current=None    # the current instance of Base
FULLSCREEN="fullscreen" # const !

try:
    if not getattr( sys, 'frozen', False ): #bypass uvloop in frozen app (wait pyinstaller hook)
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ModuleNotFoundError:
    pass

# helpers
#############################################################
exposed={}
def expose( f ):    # decorator !
    global exposed
    exposed[f.__name__]=f
    return f

def isFree(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.bind(("127.0.0.1", int(port)))
        return True
    except socket.error as e:
        return False
    finally:
        s.close()


def path(f):
    if hasattr(sys,"_MEIPASS"): # when freezed with pyinstaller ;-)
        return os.path.join(sys._MEIPASS,f)
    else:
        return f

def log(*a):
    if current and current._isLog: print(*a)

def getChrome():
    def getExe():
        if sys.platform in ['win32', 'win64']:
            return find_chrome_win()
        elif sys.platform == 'darwin':
            return find_chrome_mac()

    exe=getExe()
    if exe:
        return webbrowser.GenericBrowser(exe)
    else:
        webbrowser._tryorder=['google-chrome','chrome',"chromium","chromium-browser"]
        try:
            return webbrowser.get()
        except webbrowser.Error:
            return None

def find_chrome_win():
    import winreg #TODO: pip3 install winreg
    reg_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe'
    for install_type in winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE:
        try:
            with winreg.OpenKey(install_type, reg_path, 0, winreg.KEY_READ) as reg_key:
                return winreg.QueryValue(reg_key, None)
        except WindowsError:
            pass

def find_chrome_mac():
    default_dir = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    if os.path.exists(default_dir):
        return default_dir

def openApp(url,fullScreen=False):
    chrome=getChrome()
    if chrome:
        args=["--app="+url]
        if fullScreen: args.append("--start-fullscreen")
        if tempfile.gettempdir():
            args.append('--user-data-dir=%s' % os.path.join(tempfile.gettempdir(),".wuyapp"))
        if isinstance(chrome,webbrowser.GenericBrowser):
            chrome.args=args
            return chrome.open(url, new=1, autoraise=True)
        else:
            return chrome._invoke(args,1,1)
            

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
jar = aiohttp.CookieJar(unsafe=True)

class Response:
    def __init__(self,status,data=None,headers={}):
        self.status=status
        self.headers=dict(headers)
        self.content=data

async def request(url,data=None,headers={}):    # mimic urllib.Request() (GET & POST only)
    async with aiohttp.ClientSession(cookie_jar=jar) as session:
        try:
            if data:
                async with session.post(url,data=data,headers=headers,ssl=False) as resp:
                    return Response(resp.status,await resp.text(), resp.headers)
            else:
                async with session.get(url,headers=headers,ssl=False) as resp:
                    return Response(resp.status,await resp.text(), resp.headers)
        except aiohttp.client_exceptions.ClientConnectorError as e:
            return Response(None,str(e))
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


# Async aiohttp things (use current)
#############################################################
async def wsSend( ws, **kargs ):
    log("< send:",kargs)
    await ws.send_str( json.dumps( kargs ) )


async def asEmit(event,args,exceptMe=None):
    global current
    for ws in current._clients:
        if id(ws) != id(exceptMe):
            await wsSend(ws,event=event, args=args )

async def handleProxy(req): # proxify "/_/<url>" with headers starting with "set-"
    url = req.match_info.get("url",None)
    if req.query_string: url=url+"?"+req.query_string
    headers={ k[4:]:v for k,v in req.headers.items() if k.lower().startswith("set-")}
    r=await request( url, data=req.has_body and (await req.text()),headers=headers )
    log(". serve proxy url",url,headers,":",r.status)
    return web.Response(status=r.status or 0,text=r.content, headers=r.headers)

async def handleWeb(req): # serve all statics from web folder
    file = path('./web/'+req.match_info.get('path', "index.html"))
    if current and "/%s."%current._name in file and current.__doc__ is not None:
        return web.Response(status=200,body='<script src="wuy.js"></script>\n'+current.__doc__,content_type="text/html")
    elif os.path.isfile(file):
        log("- serve static file",file)
        return web.FileResponse(file)
    else:
        log("! 404 on",file)
        return web.Response(status=404,body="file not found")


async def handleJs(req): # serve the JS
    log("- serve wuy.js",current._size and ("(with resize to "+str(current._size)+")") or "")

    name=os.path.basename(sys.argv[0])
    if "." in name: name=name.split(".")[0]
    js="""
document.addEventListener("DOMContentLoaded", function(event) {
    %s
    %s
},true)

function setupWS( cbCnx ) {

    var ws=new WebSocket( window.location.origin.replace("http","ws")+"/ws" );

    ws.onmessage = function(evt) {
      var r = JSON.parse(evt.data);
      if(r.uuid) // that's a response from call py !
          document.dispatchEvent( new CustomEvent('wuy-'+r.uuid,{ detail: r} ) );
      else if(r.event){ // that's an event from anywhere !
          document.dispatchEvent( new CustomEvent(r.event,{ detail: r.args } ) );
      }
    };

    ws.onclose = function(evt) {
        console.log("disconnected");
        cbCnx(null);
        %s
    };
    ws.onerror = function(evt) {cbCnx(null);};
    ws.onopen=function(evt) {
        console.log("Connected",evt)
        cbCnx(ws);
    }

    return ws;
}

var wuy={
    _ws: setupWS( function(ws){wuy._ws = ws; document.dispatchEvent( new CustomEvent("init") )} ),
    on: function( evt, callback ) {     // to register an event on a callback
        document.addEventListener(evt,function(e) { callback(...e.detail) })
    },
    emit: function( evt, data) {        // to emit a event to all clients (except me), return a promise when done
        var args=Array.prototype.slice.call(arguments)
        return wuy._call("emit", args)
    },
    _call: function( method, args ) {
        var cmd={
            command:    method,
            args:       args,
            uuid:       method+"-"+Math.random().toString(36).substring(2), // stamp the exchange, so the callback can be called back (thru customevent)
        };

        if(wuy._ws) {
            wuy._ws.send( JSON.stringify(cmd) );

            return new Promise( function (resolve, reject) {
                document.addEventListener('wuy-'+cmd.uuid, function handler(x) {
                    this.removeEventListener('wuy-'+cmd.uuid, handler);
                    var x=x.detail;
                    if(x && x.result)
                        resolve(x.result)
                    else if(x && x.error)
                        resolve(x.error)
                });
            })
        }
        else
            return new Promise( function (resolve, reject) {
                reject("not connected");
            })
    },
    fetch: function(url,obj) {
        var h={"cache-control": "no-cache"};    // !!!
        if(obj && obj.headers)
            Object.keys(obj.headers).forEach( function(k) {
                h["set-"+k]=obj.headers[k];
            })
        var newObj = Object.assign({}, obj)
        newObj.headers=h;
        newObj.credentials= 'same-origin';
        return fetch( "/_/"+url,newObj )
    },
};
""" % (
        current._size and "window.resizeTo(%s,%s);"%(current._size[0],current._size[1]) or "",
        'document.title="%s";'%name,
        current._closeIfSocketClose and "window.close()" or "setTimeout( function() {setupWS(cbCnx)}, 1000);"
    )

    if current._kwargs:
        for k,v in current._kwargs.items():
            j64=str(base64.b64encode(bytes(json.dumps(v),"utf8")),"utf8")   # thru b64 to avoid trouble with quotes or strangers chars
            js+="""\nwuy.%s=JSON.parse(atob("%s"));""" % (k,j64)

    for k in current._routes.keys():
        js+="""\nwuy.%s=function(_) {return wuy._call("%s", Array.prototype.slice.call(arguments) )};""" % (k,k)

    return web.Response(status=200,text=js)

async def wshandle(req):
    global current
    ws = web.WebSocketResponse()
    await ws.prepare(req)
    current._clients.append(ws)
    try:
        async for msg in ws:
            if msg.type == web.WSMsgType.text:
                try:
                    o=json.loads( msg.data )
                    log("> RECEPT",o)
                    if o["command"] == "emit":
                        event, *args = o["args"]
                        await asEmit( event, args, ws) # emit to everybody except me
                        r=dict(result = args)           # but return the same content sended, thru the promise
                    else:
                        ret=current._routes[o["command"]]( *o["args"] )
                        if ret and asyncio.iscoroutine(ret):
                            log(". ASync call",o["command"])

                            async def waitReturn( coroutine,uuid ):
                                try:
                                    ret=await coroutine
                                    m=dict(result=ret, uuid=uuid)
                                except Exception as e:
                                    m=dict(error=str(e), uuid=uuid)
                                    print("="*40,"in ASync",o["command"])
                                    print(traceback.format_exc().strip())
                                    print("="*40)
                                await wsSend(ws, **m )

                            asyncio.ensure_future( waitReturn(ret,o["uuid"]) )
                            continue # don't answer yet (the coroutine will do it)

                        r=dict(result = ret )
                except Exception as e:
                    r=dict(error = str(e))
                    print("="*40,"on Recept",msg.data)
                    print(traceback.format_exc().strip())
                    print("="*79)

                if "uuid" in o: r["uuid"]=o["uuid"]

                await wsSend(ws, **r )
            elif msg.type == web.WSMsgType.close or msg.tp == web.WSMsgType.error:
                break
    finally:
        current._clients.remove( ws )

    if current._closeIfSocketClose: exit()
    return ws

def emit(event,*args):   # sync version of emit for py side !
    asyncio.ensure_future( asEmit( event, args) )

def exit():         # exit method
    async def handle_exception(task):
        try:
            await task.cancel()
        except Exception:
            pass

    for task in asyncio.Task.all_tasks():
        asyncio.ensure_future(handle_exception(task))

    asyncio.get_event_loop().stop()
    asyncio.set_event_loop(asyncio.new_event_loop())    # renew, so multiple start are availables

    log("exit")
    sys.exit(0)

# WUY routines
#############################################################
class Base:
    FULLSCREEN="fullscreen"

    _routes={}
    _clients=[]
    _closeIfSocketClose=False
    _isLog=False
    _size=None
    _kwargs={}  # Window/Server only
    def __init__(self,instance,exposed={}):
        if isinstance(instance,Base):
            self._name=instance.__class__.__name__
            self._routes={n:v for n, v in inspect.getmembers(instance, inspect.ismethod) if isinstance(v,types.MethodType) and "bound method %s."%self._name in str(v)}  #  TODO: there should be a better way to discover class methos
        else: # old style (eel)
            self._name=instance # aka page name
            self._routes=exposed


    def _run(self,port=DEFAULT_PORT,app=None,log=True):   # start method (app can be True, (width,size), ...)
        global current,application

        try:
            os.chdir(os.path.split(sys.argv[0])[0])
        except:
            pass

        current=self    # set current !

        self._isLog=log

        globals()["log"]("Will accept : %s" % ", ".join(self._routes.keys()) )  #TODO: not neat

        page=self._name+".html"

        

        # create startpage if not present and no docstring
        if self.__doc__ is None:
            startpage=path("./web/"+page)
            if not os.path.isfile(startpage):
                if not os.path.isdir(os.path.dirname(startpage)):
                    os.makedirs(os.path.dirname(startpage))
                with open(startpage,"w+") as fid:
                    fid.write('''<script src="wuy.js"></script>\n''')
                    fid.write('''Hello Wuy'rld ;-)''')
                print("Create 'web/%s', just edit it" % os.path.basename(startpage))

        if app:
            self._closeIfSocketClose=True
            host="localhost"
            if application is None:
                while not isFree(host,port):
                    port+=1
            url = "http://%s:%s/%s?%s"% (host,port,page,uuid.uuid4().hex)

            if type(app)==tuple and len(app)==2:    #it's a size tuple : set it !
                self._size=app

            def runApp(url):
                ok=openApp(url,app==FULLSCREEN)
                if not ok:
                    print("Can't find Chrome on your desktop ;-(")
                    os._exit(-1)

            t = Thread(target=runApp, args=(url,))
            t.start()   #TODO: what to do if no browser is launcher ???

        else:
            host="0.0.0.0"

        self.init()

        if application is None:
            application=web.Application()
            application.add_routes([
                web.get('/ws',      wshandle),
                web.get('/wuy.js',  handleJs),
                web.get('/',        handleWeb),
                web.get('/{path}',  handleWeb),
                web.route("*",'/_/{url:.+}',handleProxy),
            ])
            try:
                if self._closeIfSocketClose: # app-mode, don't shout "server started,  Running on, ctrl-c"
                    web.run_app(application,host=host,port=port,print=lambda *a,**k: None)
                else:
                    web.run_app(application,host=host,port=port)
            except KeyboardInterrupt:
                exit()

    def emit(self,*a,**k):  # emit available for all
        emit(*a,**k)

    def init(self):
        pass

class Window(Base):
    size=True   # or a tuple (wx,wy)
    def __init__(self,port=DEFAULT_PORT,log=True,**kwargs):
        super().__init__(self)
        self.__dict__.update(kwargs)
        self._kwargs=kwargs
        self._run(app=self.size,port=port,log=log)

    def exit(self): # exit is available for Window !!
        exit()

class Server(Base):
    def __init__(self,port=DEFAULT_PORT,log=True,**kwargs):
        super().__init__(self)
        self.__dict__.update(kwargs)
        self._kwargs=kwargs
        self._run(app=False,port=port,log=log)


def start(page="index",port=DEFAULT_PORT,app=None,log=True):
    """ old style run with exposed methods (like eel)
            'app' can be True, (width,size) (for window-like(app))
            'app' can be None, False (for server-like)
    """
    b=Base(page,exposed)
    b._run(port=port,app=app,log=log)

if __name__=="__main__":
    openApp("https://github.com/manatlan/wuy")
