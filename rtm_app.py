import socketio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

templates = Jinja2Templates(directory="templates")
sio = socketio.AsyncServer(async_mode='asgi') # cors_allowed_origins='*',
app = FastAPI()
# https://github.com/tiangolo/fastapi/issues/129
# https://github.com/pyropy/fastapi-socketio
sio_app = socketio.ASGIApp(sio, static_files={'/': 'page.html'})
app.mount('/sio', sio_app)
#app.mount('/socket.io')
app.mount("/static", StaticFiles(directory="templates"), name="static")


@sio.event
async def connect(sid, environ, auth=None):
    print("connect ", sid)


@sio.on('message')
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('response', data)

USER_SID2NAME = {}

@sio.on('who_are_you')
async def identify_user(sid, data):
    global USER_SID2NAME
    USER_SID2NAME[str(sid)] = data
    print('sid: ', sid, ' is a user: ', data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


@app.get("/chat", response_class=HTMLResponse)
def main_func(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
