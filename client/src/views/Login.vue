<template>
  <form @submit.prevent="Login" name="LoginForm">
    <h1>Login</h1>
    <div class="form-input">
      <input type="email" name="email" placeholder="email" v-model="email" />
    </div>
    <div class="form-input">
      <input
        type="password"
        name="passowrd"
        placeholder="password"
        v-model="password"
      />
    </div>
    <button type="submit">Sing in</button>
  </form>
</template>

<style scoped>
form {
  align-self: flex-start;
  display: grid;
  justify-items: center;
  align-items: center;
  height: 17rem;
  width: 14rem;
  top: 20%;
  left: 36%;
  position: absolute;
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
  height: 3rem;
}
.form-input {
  margin-bottom: 10px;
}
</style>
<script>
export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    Login: function () {
    let loginData = {
      email:this.email,
      password:this.password
    }
     fetch('http://127.0.0.1:5000/api/auth/login',{
       method:'POST',
       headers:{
         'Content-Type': 'application/json;utf-8'
       },
       body:JSON.stringify(loginData)
     }).then(response=>{
       if (response.ok){
          this.$router.push('/')
       }else{
         console.log('нема юзера и праоля');
       }
     }).catch(e=>console.error(e))
    },
  },
};
</script>