import { createRouter, createWebHistory } from 'vue-router';
import Ping from '../components/Ping.vue';
import LoginPage from '../components/LoginPage.vue';
import ChatPage from '../components/ChatPage.vue';

const routes = [
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/',
    name: 'LoginPage',
    component: LoginPage,
  },
  {
    path: '/chat',
    name: 'ChatPage',
    component: ChatPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
