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
