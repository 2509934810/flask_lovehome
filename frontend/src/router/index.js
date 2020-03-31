import Vue from 'vue'
import Router from 'vue-router'
import index from '@/views/index.vue'
import Index1 from '@/views/Homeindex'
import login from '@/views/Auth/Login.vue'
import register from '@/views/Auth/Register.vue'
import myinfo from '@/views/User/myInfo.vue'
import notFindPage from '@/views/error/404.vue'
// import userSec from '@/views/User/userSec.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/homeservice',
      name: 'homeservice',
      component: Index1
    },
    {
      path: '/login',
      name: 'login',
      component: login
    },
    {
      path: '/register',
      name: 'register',
      component: register
    },
    {
      path: '/user',
      component: myinfo
    },
    {
      path: '*',
      component: notFindPage
    }
  ]
})
