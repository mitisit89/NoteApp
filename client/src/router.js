import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Page2 from '@/views/Page2'

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
        }
    ]
})