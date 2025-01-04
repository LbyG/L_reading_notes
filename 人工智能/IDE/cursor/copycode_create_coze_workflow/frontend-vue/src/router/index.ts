import { createRouter, createWebHistory } from 'vue-router'
import WorkflowEditor from '../components/WorkflowEditor.vue'

const routes = [
  {
    path: '/',
    name: 'WorkflowEditor',
    component: WorkflowEditor
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router 