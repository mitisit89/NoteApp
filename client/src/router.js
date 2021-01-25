import Vue from "vue";
import Router from "vue-router";
import Home from "@/views/Home";
import Page2 from "@/views/Page2";
import CreateNote from "@/views/CreateNote";
import WellcomePage from "@/views/WellcomePage"
Vue.use(Router);
//переделать 



export default new Router({
  mode: "history",
  routes: [
    {
      path:'/',
      component:WellcomePage
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
  ],
});
