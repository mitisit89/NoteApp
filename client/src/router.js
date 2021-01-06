import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Page2 from "@/views/Page2";
import CreateNote from "@/views/CreateNote";
import store from "@/store";
Vue.use(Router);
//переделать 
const ifNotLogin = (to, from, next) => {
  if (!store.getters.getLoginStatus) {
    next();
    return;
  }
  next("/");
};
const ifLogin = (to, from, next) => {
  if (store.getters.getLoginStatus) {
    next();
    return;
  }
  next("/home");
};

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/home",
      component: Home,
    },
    {
      path: "/page2",
      component: Page2,
      beforeEnter: ifNotLogin,
    },
    {
      path: "/create",
      component: CreateNote,
      beforeEnter: ifLogin,
    },
  ],
});
