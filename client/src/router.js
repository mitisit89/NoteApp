import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home'
import Notes from '@/views/Notes'
Vue.use(Router)

export default new Router({
    mode:'history',
    routes:[
        {
            path:'/',
            component:Home
        },{
            path:'/notes',
            component:Notes
        }
    ]
})