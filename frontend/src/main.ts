import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
// import './style.css'
import './assets/css/IU_brand.css'
import App from './App.vue'
import LoginPage from './components/LoginPage.vue'
import StatsWrapper from './components/StatsWrapper.vue'

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: LoginPage },
        { path: '/stats', component: StatsWrapper },
    ]
})

createApp(App).use(router).mount('#app')
