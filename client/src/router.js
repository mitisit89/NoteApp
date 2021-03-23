import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Page2 from "@/views/Page2";
import CreateNote from "@/views/CreateNote";
import WelcomePage from "@/views/WelcomePage";
import EditNote from "@/views/EditNote"
Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      component: WelcomePage,
    },

    {
      path: "/home",
      component: Home,
    },
    {
      path: "/page2",
      component: Page2,
    },
    {
      path: "/create",
      component: CreateNote,
    },
    {
      path:'/edit',
      component:EditNote,
    }
  ],
});
