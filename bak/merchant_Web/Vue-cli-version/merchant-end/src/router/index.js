import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Login from '@/components/login'
import RestaurantInfo from '@/components/RestaurantInfo'
import Menu from '@/components/Menu'
import Order from '@/components/Order'
import QRcode from '@/components/QRcode'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/',
      name: 'Login',
      component:Login
    },
    {
      path: '/home',
      component: Home,
      children: [
      	{
      		path: 'restaurantinfo',
      		component: RestaurantInfo
      	},
      	{
      		path: 'menu',
      		component: Menu
      	},
        {
          path: 'generate_qrcode',
          component: QRcode
        },
      	{
      		path: 'order',
      		component: Order
      	}
      ]
    },
    {
    	path:'*',
    	redirect: '/'
    }
  ]
})
