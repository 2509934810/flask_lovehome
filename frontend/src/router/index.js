import Vue from 'vue'
import Router from 'vue-router'
import Index1 from '@/views/Homeindex'
import mid from '@/components/JiaZheng/mid.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/homeservice',
      name: 'homeservice',
      component: Index1
    },
    {
      path: '/mid',
      name: 'mid',
      component: mid
    }
  ]
})
