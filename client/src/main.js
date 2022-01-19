import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import chatStore from './components/ChatStore.vue';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';

createApp(App)
  .use(chatStore)
  .use(router)
  .mount('#app');
