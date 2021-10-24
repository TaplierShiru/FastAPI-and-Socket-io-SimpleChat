import socketio
from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

X_AUTHORIZATION = 'X-Authorization'

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


class RegisterValidator(BaseModel):
    username: str


@app.get('/api/user')
def get_user(request: Request):
    return request.cookies.get(X_AUTHORIZATION)


@app.post("/api/register")
def register_user(user: RegisterValidator, response: Response):
    response.set_cookie(key=X_AUTHORIZATION, value=user.username, httponly=True)


@app.get('/')
def get_home(request: Request):
    return templates.TemplateResponse('home.html', {"request": request})


@app.get('/chat')
def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})


@app.get("/hello", response_class=HTMLResponse)
def main_func(request: Request):
    return templates.TemplateResponse(
        "page.html",
        {"request": request}
    )

app.mount('/', sio_app)