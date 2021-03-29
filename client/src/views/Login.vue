<template>
  <form @submit.prevent="Login" class="box is-mobile"  name="LoginForm">
    <b-field label='Email' >
      <b-input type="email" name="email"  v-model="email" />
    </b-field>
    <b-field label='Password' >
      <b-input
        type="password"
        name="passowrd"
        placeholder="password"
        v-model="password"
      />
    </b-field>
    <b-button type="is-success" native-type=submit>Sing in</b-button>
  </form>
</template>


<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    ...mapActions(["authLogin"]),
    Login() {
      this.authLogin({
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>
