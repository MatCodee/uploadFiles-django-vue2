import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import UploadPage from "../views/UploadPage"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/upload',
    name: 'Upload',
    component: UploadPage
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
