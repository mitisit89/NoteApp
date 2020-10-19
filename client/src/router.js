import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Page2 from '@/views/Page2'
import Login from '@/views/Login'
import CreateNote from '@/views/CreateNote'
import Registration from '@/views/Registration'

Vue.use(Router)

export default new Router({
    mode: 'history',
    routes: [
        {
            path: '/',
            component: Home
        },
        {
            path: '/page2',
            component: Page2
        },
        {
            path: '/login',
            component: Login
        },
        {
            path: '/registration',
            component: Registration
        },
        {
            path: '/create',
            component:CreateNote
        }
    ]
})