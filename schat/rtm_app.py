import logging
import socketio
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# Logger
logging.basicConfig(
    level=logging.DEBUG, format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s'
)
log = logging.getLogger('nbt')


# Init stuff for further usage
templates = Jinja2Templates(directory="templates")
sio = socketio.AsyncServer(async_mode='asgi') # cors_allowed_origins='*',
app = FastAPI()

# There is some problem about how to start socketio with FastAPI
# I found some help in these links:
# https://github.com/tiangolo/fastapi/issues/129
# https://github.com/pyropy/fastapi-socketio
# After reading them, I wrote some lines below and its works as it should be!
sio_app = socketio.ASGIApp(
    sio,
    static_files={'/': 'page.html'} # I.e. link html page which should be communicated with server ??? (not sure here)
)
app.mount('/sio', sio_app) # Mount socket-io app to some page

# Mount templates
app.mount("/static", StaticFiles(directory="templates"), name="static")


@sio.event
async def connect(sid, environ, auth=None):
    log.debug(f"Connect with {sid}")


@sio.on('message')
async def chat_message(sid, data):
    session_data = await sio.get_session(sid)
    log.debug(f"Take message username={session_data['username']}, message={data}")
    await sio.emit('response', data)


@sio.on('who_are_you')
async def identify_user(sid, data):
    await sio.save_session(sid, {'username': data})
    log.debug(f"Identify user with sid={sid} and username={data}")


@sio.on("change_nickname")
async def change_nickname(sid, data):
    await sio.save_session(sid, {'username': data})
    log.debug(f"User change nickname to {data}")


@sio.event
def disconnect(sid):
    log.debug(f"Disconnect user with sid={sid}")


@app.get("/v2")
def read_main():
    return {"message": "Hello World"}


@app.get("/chat", response_class=HTMLResponse)
def main_func(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )
