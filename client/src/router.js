import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Page2 from "@/views/Page2";
import Login from "@/views/Login";
import CreateNote from "@/views/CreateNote";
import Registration from "@/views/Registration";
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
  next("/login");
};

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      component: Home,
    },
    {
      path: "/page2",
      component: Page2,
      beforeEnter: ifNotLogin,
    },
    {
      path: "/login",
      component: Login,
      beforeEnter: ifNotLogin,
    },
    {
      path: "/registration",
      component: Registration,
      beforeEnter: ifNotLogin,
    },
    {
      path: "/create",
      component: CreateNote,
      beforeEnter: ifLogin,
    },
  ],
});
