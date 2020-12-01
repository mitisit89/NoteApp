<template>
  <nav id="navigation">
    <div class="nav-menu">
      <ul class="nav-list">
        <li class="nav-link">
          <router-link to="/">Главная</router-link>
        </li>
        <li class="nav-link">
          <router-link to="/page2">Page2</router-link>
        </li>
        <template v-if="getIslogin === 'logged'">
          <li class="nav-link" v-if="checkLogin === true">
            <router-link to="/create">create</router-link>
          </li>
          <li class="nav-link">
            <a v-on:click="Logout" href="/">Выход</a>
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
    <button id="search" type="submint">
      <span class="material-icons"> search </span>
    </button>
  </nav>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
  computed:mapGetters(["getIslogin"]),
  methods: {
    ...mapActions(["logout"]),
    Logout() {
      this.logout();
      this.$router.push("/");
    },
   
  },
};
</script>

<style>
#navigation {
  display: flex;
  flex-flow: row;
  background-color: #3d3d3f;
  color: white;
  padding: 10px;
  margin: 10px;
  position: relative;
  align-content: space-between;
  border-radius: 10px;
  position: fixed;
  z-index: 1000;
}

.nav-list,
.auth-list {
  display: inline-flex;
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