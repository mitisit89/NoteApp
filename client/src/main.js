import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import Buefy from 'buefy'
Vue.config.productionTip = false
Vue.use(Buefy)
new Vue({
    store,
    router,
  
    render: function (h) {
        return h(App)
    },
}).$mount('#app')
