<template>
  <div id="app">
      <router-view />
    </div>
</template>
<script>
import "material-design-icons/iconfont/material-icons.css";
import "buefy/dist/buefy.css";
export default {};
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Ubuntu&display=swap&subset=cyrillic-ext");

*,
::before,
::after {
  box-sizing: border-box;
}

html,
body {
  font-family: "Ubuntu", sans-serif;
  background-color: #fafafa;
  margin: 0;
  padding: 0;
}

a {
  text-decoration: none;
}

li {
  list-style-type: none;
}
</style>
