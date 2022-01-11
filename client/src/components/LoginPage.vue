<template>
  <div class="chat-body card">
    <div class="card-body">
      <h4 class="card-title text-center"> Chat App </h4>
      <hr>
      <form class="form-inline" id="user-form">
        <label for="userNickname">Your nickname:</label>
        <input v-model="nickname" type="text" id="input-nickname"
            class="form-control" placeholder="Enter your name">
        <button type="button" @click="startChat">Start Chat</button>
      </form>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import createCookie from '../cookie_funcs/createCookie';

export default {
  name: 'LoginPage',
  data() {
    return {
      nickname: 'None',
    };
  },
  methods: {
    startChat() {
      console.log(this.nickname);
      alert(`Start chat with user nickname=${this.nickname}!`);

      const path = 'http://127.0.0.1:80/api/register';
      axios.post(path, {
        username: this.nickname,
      }).then(
        (res) => {
          console.log(res);
          createCookie('nickname', this.nickname, 7);
          window.location.href = '/chat';
        },
      ).catch(
        (error) => {
          console.log(error);
        },
      );
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card {
  position: absolute;
  width: 95%;
  height: 80%;
  box-shadow: 0px 0px 5px gray;
  left: 2.5%;
  top: 5%;
}
#user-form {
  position: absolute;
  top: 20%;
  left: 50%;
  transform: translateX(-50%);
}
#user-form input {
  width: 400px;
  padding-right: 30%;
}
#user-form button {
  position: absolute;
  left: 75%;
  margin-left: 2px;
}
</style>
