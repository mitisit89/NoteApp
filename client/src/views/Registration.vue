<template>
  <form @submit.prevent="Registration">
    <h1>Registration</h1>
    <input
      class="form-input"
      type="text"
      name=""
      id=""
      placeholder="Username"
      v-model="username"
    />
    <input type="email" placeholder="Email" v-model="email" />
    <span v-show="password !== confirm_password && confirm_password !== ''"
      >Пароли не совпадают</span
    >
    <input type="password" placeholder="Password" v-model="password" />
    <input
      type="password"
      placeholder="Confirm password"
      v-model="confirm_password"
    />
    <button type="submit">Регистрация</button>
  </form>
</template>

<style scoped>
form {
  background-color: #3d3d3f;
  border: none;
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 17rem;
  width: 14rem;
  top: 20%;
  left: 36%;
  position: absolute;
  flex-direction: column;
}
h1 {
  color: white;
}
button {
  width: 14rem;
  height: 2rem;
  color: white;
  border-radius: 90px;
  border: none;
  background: #3d3d3f;
  display: inline-block;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}
input {
  border: none;
  height: 3rem;

  margin: 10px;
  z-index: 1;
  border-radius: 1px;
}
.form-input {
  margin-bottom: 10px;
}
span {
  color: red;
}
</style>
<script>
import { mapActions } from "vuex";
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirm_password: "",
    };
  },
  methods: {
    ...mapActions(["authRegistration"]),
    Registration() {
      this.authRegistration({
        username: this.username,
        email: this.email,
        password: this.password,
      });
    },
  },
};
</script>
