import logging

import socketio
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

X_AUTHORIZATION = 'X-Authorization'

# Logger
logging.basicConfig(
    level=logging.DEBUG, format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s'
)
log = logging.getLogger('nbt')

# Init stuff for further usage
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=["*"]) # cors_allowed_origins='*',
app = FastAPI()
# Add cors
origins = [
    "http://localhost:8080",
    "http://localhost:8080/chat",
    "http://localhost:8080/*",
    "http://localhost:8080/socket.io",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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



@sio.event
async def connect(sid, environ, auth=None):
    log.debug(f"Connect with {sid}")


@sio.on('message')
async def chat_message(sid, data):
    session_data = await sio.get_session(sid)
    log.debug(f"Take message username={session_data['username']}, message={data['message']}")
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


class RegisterValidator(BaseModel):
    username: str


@app.get('/api/user')
def get_user(request: Request):
    return request.cookies.get(X_AUTHORIZATION)


@app.post("/api/register")
async def register_user(user: RegisterValidator, response: Response):
    response.set_cookie(key=X_AUTHORIZATION, value=user.username, httponly=True)
    log.debug(f"User register with username={user.username}")
    return user.json()


@app.get("/ping")
async def test_ping():
    return "Hello from backend!"
