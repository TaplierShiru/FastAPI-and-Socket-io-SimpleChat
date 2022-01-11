<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>

import axios from 'axios';

export default {
  name: 'Ping',
  data() {
    return { msg: 'Empty' };
  },
  methods: {
    getMessage() {
      const path = 'http://127.0.0.1:80/ping';
      axios.get(path).then(
        (res) => {
          console.log(res);
          this.msg = res.data;
        },
      ).catch(
        (error) => {
          console.log(error);
        },
      );
    },
  },
  created() {
    this.getMessage();
  },
};

</script>
