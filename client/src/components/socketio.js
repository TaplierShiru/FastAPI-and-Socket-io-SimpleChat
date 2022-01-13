import { io } from 'socket.io-client';

/*
const socketio = io(
  'http://127.0.0.1:3117/socket.io', {
    //    autoConnect: false,
    // transports: ['websocket', 'polling', 'flashsocket'],
  },
);
*/

const socketio = io(
  'ws://127.0.0.1:3117', {
    path: '/ws/socket.io',
    //    autoConnect: false,
    transports: ['websocket', 'polling'],
  },
);

export default socketio;
