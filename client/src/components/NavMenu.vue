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
import { mapActions } from "vuex";
export default {
  methods: mapActions(["logout"]),
};
</script>

<style>
header {
  position: relative;
  z-index: 1000;
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