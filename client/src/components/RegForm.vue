<template>
  <form class="box" @submit.prevent="onSub">
    <b-field label="Email">
      <b-input type="email" v-model="email" maxlength="30" />
    </b-field>
    <b-field label="Username">
      <b-input v-model="username" />
    </b-field>
    <b-field label="Password">
      <b-input type="password" v-model="password" password-reveal> </b-input>
    </b-field>
    <b-button class="button is-primary" native-type=submit>Подтвердить</b-button>
  </form>
</template>

<script>
export default {
  data() {
    return {
      email: "",
      username: "",
      password: "",
    };
  },
  methods: {
    onSub() {
      const newUser = {
        email: this.email,
        username: this.username,
        password: this.password,
      };
      this.$emit("add-new-user", newUser);
    },
  },
};
</script>