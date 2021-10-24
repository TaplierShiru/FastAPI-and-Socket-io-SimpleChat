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
    session_data = await sio.get_session(sid)
    print(f"username={session_data['username']}, message={data}")
    await sio.emit('response', data)


@sio.on('who_are_you')
async def identify_user(sid, data):
    await sio.save_session(sid, {'username': data})
    print('sid: ', sid, ' is a user: ', data)


@sio.on("change_nickname")
async def change_nickname(sid, data):
    await sio.save_session(sid, {'username': data})
    print(f'new nickname={data}')


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
