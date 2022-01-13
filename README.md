# FastAPI-and-Socket-io-SimpleChat
Simple chat web page using FastAPI and python-socket-io frameworks.
Main usage of this project - learn how to use socket-io stuff with python and JavaScript,
there is can be some issue with code - so, be aware.

# How start app. 
Clone this repo. You can do that with next command:

```
git clone https://github.com/TaplierShiru/FastAPI-and-Socket-io-SimpleChat.git
cd FastAPI-and-Socket-io-SimpleChat
```

## Option 1. Start server and client without docker
## Setup server
### Update python environment
Install libraries for server with next command:
```
cd server
pip install -r requirements.txt
```

In order to start server, type next command

```
uvicorn app_chat:app --host 0.0.0.0 --port 3117
```

Check server status on page: `http://127.0.0.1:8000/api/ping`. 
On this page you must see a message from server.
If you can see it - then everything is cool.

## Setup client
Setup npm for project with next commands:

```
cd client
npm install
npm run serve
```

In a browser open page `http://localhost:8080/` 
there you can see page of the app, if everything is set up well.

## Option 2. Run two dockers
You must install docker and run two separate dockers with next commands:
```
cd server
docker build -t backend-python .
docker run -d -p 3117:3117 backend-python
cd client
docker build . -t my-app
docker run -d -p 8080:80 my-app
```

In a browser open page `http://localhost:8080/` 
there you can see page of the app, if everything is set up well.

## Option 3. Run compose-docker
You must install docker with compose-docker and start app with next command:
```
docker-compose -f .\docker-compose.yml up --build -d
```

Tested on Windows 10, Python 3.8, Browser - Microsoft Edge.
