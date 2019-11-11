import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import username from '@/components/username'
import userphone from '@/components/userphone'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      component: login,
    },
    {
    	path:'/',
    	redirect: '/login'
    }
  ]
})
