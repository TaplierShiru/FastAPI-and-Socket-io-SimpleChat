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
                <li class="single-mess" v-for="(user_s, index) in users_info"
                    v-bind:key="`key-${index}`">
                        <p><strong>{{ user_s.nickname }}</strong> <span>{{ user_s.text }}</span></p>
                </li></transition-group>
            </ul></div>
            <form class="form-inline" id="chat-form">
                <input v-model="message" type="text"
                    class="form-control" placeholder="Write your message">
                <button type="button" @click="sendMessage">Send</button>
            </form>
        </div>
    </div>
</template>
<script>

// import axios from 'axios';
import io from 'socket.io-client';
import readCookie from '../cookie_funcs/readCokie';

const socket = io('http://127.0.0.1:80');

function getUsernick() {
  return readCookie('nickname');
}
socket.emit('who_are_you', getUsernick);
socket.on('connect', async () => {
  console.log('Connected!');
  socket.emit('who_are_you', getUsernick);
});

socket.on('disconnect', () => {
  console.log('Lost connection to the server!');
});

export default {
  name: 'ChatPage',
  data() {
    return {
      users_info: [
        { nickname: 'Pite', text: 'Blalala' },
        { nickname: 'Qwe', text: '23sss' },
      ],
      username: 'unknown',
    };
  },
  methods: {
    addMessage(nickname, text) {
      this.users_info.push({
        nickname,
        text,
      });
    },
    sendMessage() {
      socket.emit('message',
        {
          sender: getUsernick(),
          message: this.message,
        });
      console.log('Message send!');
    },
  },
  created() {
    this.$nextTick(() => {
      this.username = getUsernick();
    });
  },
};
</script>
<style>

</style>
