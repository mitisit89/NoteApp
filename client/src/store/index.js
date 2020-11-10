import Vue from 'vue'
import Vuex from 'vuex'
import PostStorage from './modules/PostStorage'
Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        PostStorage
    }
})