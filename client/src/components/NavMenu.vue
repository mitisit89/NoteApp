<template>
  <header>
    <b-navbar type="is-dark">
      <template slot="start">
        <b-navbar-item tag="router-link" :to="{ path: '/home' }"
          >Home</b-navbar-item
        >
        <b-navbar-item>
          <router-link to="/page2">Page2</router-link>
        </b-navbar-item>
          <b-navbar-item tag="router-link" :to="{ path: '/create' }">
            Add
          </b-navbar-item>
          <b-navbar-item>
            <a v-on:click="logout" href="/">Выход</a>
          </b-navbar-item>
      </template>
    </b-navbar>
  </header>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
export default {
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