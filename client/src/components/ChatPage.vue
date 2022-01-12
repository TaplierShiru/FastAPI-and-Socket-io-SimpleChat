<template>
    <div class="chat-body card">
        <div class="card-body">
            <strong id="profile">{{ username }}</strong>
            <h4 class="card-title text-center"> Chat App </h4>
            <hr>
            <div id="messages"><ul style="list-style: none;">
                <transition-group name="custom-enter-transition"
                    enter-active-class="animate__animated animate__bounceInUp"
                    class="pop-up-message-transition">
                <li class="single-mess" v-for="(user_s, index) in getMessages"
                    v-bind:key="`key-${index}`">
                        <p><strong>{{ user_s.nickname }}</strong> <span>{{ user_s.text }}</span></p>
                </li></transition-group>
            </ul></div>
            <form class="form-inline fixed-bottom" id="chat-form">
                <input v-model="message" type="text"
                    class="form-control" placeholder="Write your message">
                <button type="button" @click="sendMessage">Send</button>
            </form>
        </div>
    </div>
</template>
<script>
import chatStore from './ChatStore.vue';
// import axios from 'axios';
import socketio from './socketio';
import readCookie from '../cookie_funcs/readCokie';

function getUsernick() {
  return readCookie('nickname');
}

socketio.on('connect', () => {
  socketio.emit('identify_user', { data: getUsernick() });
  console.log('Connected!');
});

socketio.on('disconnect', () => {
  console.log('Lost connection to the server!');
});
/*
socket.on('response', (data) => {
  console.log(`Response... with data=${JSON.stringify(data)}`);
  let { sender } = data;
  if (sender == getUsernick()) {
    sender = 'You';
  }
  const { message } = data;
  console.log(`Message=${message}`);
  vue_messages_handler.addMessage(sender, message);
  console.log(vue_messages_handler.users_info);
});
*/
export default {
  name: 'ChatPage',
  store: chatStore,
  data() {
    return {
      username: 'unknown',
    };
  },
  methods: {
    addMessage(nickname, text) {
      this.$store.dispatch('addMessage', { nickname, text });
    },
    sendMessage() {
      socketio.emit('message',
        {
          sender: getUsernick(),
          message: this.message,
        });
      console.log('Message send!');
    },
  },
  computed: {
    getMessages() {
      return this.$store.state.messageInfo;
    },
  },
  created() {
    this.$nextTick(() => {
      this.username = getUsernick();

      socketio.on('response', (data) => {
        console.log(`Response... with data=${JSON.stringify(data)}`);
        let { sender } = data;
        if (sender === getUsernick()) {
          sender = 'You';
        }
        const { message } = data;
        console.log(`Message=${message}`);
        this.addMessage(sender, message);
        console.log(this.getMessages);
      });
    });
  },
};
</script>
<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
html {
    background-color: #00539F;
}
body {
  font: 13px Helvetica, Arial;
  width: 800px;
  margin: 0 auto;
  background-color: #FF9500;
  padding: 0 20px 20px 20px;
  border: 5px solid black;
}
h1 {
    margin: 0;
    padding: 20px 0;
    color: #00539F;
    text-shadow: 3px 3px 1px black;
}
form {
    background: #000;
    padding: 3px;
    position: -webkit-sticky;
    position: fixed;
    bottom: 0;
    width: 75%;
    box-sizing: content-box;
}
form input {
    border: 0;
    padding: 10px;
    width: 70%;
    margin-right: 1.0%;
}
form button {
    width: 22%;
    background: rgb(255, 255, 255);
    border: none;
    padding: 10px;
}
label {
    font-size: 24px;
    text-align: center;
    color: #00539F;
    font-family: cursive;
}

#messages {
    list-style-type: none;
    padding-bottom: 0.5%;
    padding-top: 40px;
}
#messages:empty {
    list-style-type: none;
    margin: 0;
    padding-top: 40px;
}

#messages li {
    height: 40px;
    margin: 2px;
    background-color: #7FFFD4;
}
#messages li:first-child {
    margin-top: -38px;
}
</style>
