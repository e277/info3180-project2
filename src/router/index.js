import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import RegisterUser from '../components/RegisterUser.vue'
import LoginUser from '../components/LoginUser.vue'
import LogoutUser from '../components/LogoutUser.vue'
import AddNewPostView from '../views/AddNewPostView.vue';
import ExploreView from '../views/ExploreView.vue';
import ProfileView from '../views/ProfileView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'RegisterUser',
      component: RegisterUser
    },
    {
      path: '/login',
      name: 'LoginUser',
      component: LoginUser
    },
    {
      path: '/logout',
      name: 'LogoutUser',
      component: LogoutUser
    },
    {
      path:'/post/create',
      name: 'AddNewPostView',
      component: AddNewPostView,
    },
    {
      path:'/explore',
      name: 'ExploreView',
      component: ExploreView,
    },
    {
      path:'/profile/:user_id',
      name: 'ProfileView',
      component: ProfileView,
    },
  ]
})

export default router
