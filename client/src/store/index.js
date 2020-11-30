import Vue from 'vue'
import Vuex from 'vuex'
import PostStorage from './modules/PostStorage'
import AuthStorage  from './modules/AuthStorage'
Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        PostStorage,
        AuthStorage 
    }
})