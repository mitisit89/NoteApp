<template>
  <header>
    <div class="nav-toggle">
      <span  class="material-icons" v-on:click='show = !show'  > menu </span>
    </div>
    <nav id="navigation" v-show="!show">
      <span v-on:click='show = !show' class="material-icons"> close </span>
      <div class="nav-menu">
        <ul class="nav-list">
          <li class="nav-link">
            <router-link to="/">Главная</router-link>
          </li>
          <li class="nav-link">
            <router-link to="/page2">Page2</router-link>
          </li>
          <template v-if="getLoginStatus === 'logged'">
            <li class="nav-link">
              <router-link to="/create">create</router-link>
            </li>
            <li class="nav-link">
              <a v-on:click="logout" href="/">Выход</a>
            </li>
          </template>
          <template v-else>
            <li class="nav-link">
              <router-link to="/login">Вход</router-link>
            </li>
            <li class="nav-link">
              <router-link to="/registration">Регистрация </router-link>
            </li>
          </template>
        </ul>
      </div>
    </nav>
  </header>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  data(){
    return{
      show:true
    }
  },
  computed: mapGetters(["getLoginStatus"]),
  methods: mapActions(["logout"]),

};
</script>

<style>
header {
  position: relative;
  z-index: 1000;
}
#navigation {
  display: flex;
  flex-flow: row;
  background-color: #3d3d3f;
  color: white;
  padding: 10px;
  margin: 10px;
  position: fixed;
  align-content: space-between;
  border-radius: 10px;
  width: 300px;
  top: 0;
  left: 0;
  overflow-x: hidden;
}

.nav-list,
.auth-list {
  display: flex;
  flex-direction: column;
  justify-items: space-around;
  max-width: 1000px;
  padding: 1rem;
}

.nav-link {
  flex-flow: row wrap;
  padding: inherit;
}

.nav-link a {
  color: white;
}

.nav-menu {
  display: flex;
  align-content: inherit;
  align-content: space-between;
}
#search {
  margin: 10px 10px 10px;
  overflow: hidden;

  border: none;
}
.material-icons {
  font-family: "Material Icons";
  font-style: normal;
  font-weight: 400;
}
</style>