<template>
  <form>
    <h1>Login</h1>
    <div class="form-input">
      <input type="email" name id placeholder="email" />
    </div>
    <div class="form-input">
      <input type="password" placeholder="password" />
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
  color:white;
  border-radius: 90px;
  border: none;
  background:#3d3d3f;
  display: inline-block;
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);
}
input {
  height: 3rem;

}
.form-input {
  margin-bottom: 10px;

}
</style>