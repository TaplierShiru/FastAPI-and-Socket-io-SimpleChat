<script>
import { createStore } from 'vuex';

const chatStore = createStore({
  state: {
    messageInfo: [],
  },
  mutations: {
    addMessage(state, { nickname, text }) {
      state.messageInfo.push({ nickname, text });
    },
    logout(state) {
      state.messageInfo = [];
    },
  },
  actions: {
    addMessage(context, { nickname, text }) {
      context.commit('addMessage', { nickname, text });
    },
    clearMessages(context) {
      context.commit('logout');
    },
  },
  getters: {
    getMessageInfo: (state) => state.messageInfo,
    getLength: (state, getters) => getters.getMessageInfo.length,
  },
});

export default chatStore;
</script>
