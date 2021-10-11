import socketio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
sio = socketio.AsyncServer(async_mode='asgi') # cors_allowed_origins='*',
app = FastAPI()
# https://github.com/tiangolo/fastapi/issues/129
# https://github.com/pyropy/fastapi-socketio
sio_app = socketio.ASGIApp(sio, static_files={'/': 'page.html'})


@sio.event
def connect(sid, environ):
    print("connect ", sid)


@sio.on('message')
async def chat_message(sid, data):
    print("message ", data)
    await sio.emit('response', 'hi ' + data)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


@app.get("/hello", response_class=HTMLResponse)
def main_func(request: Request):
    return templates.TemplateResponse(
        "page.html",
        {"request": request}
    )

app.mount('/', sio_app)