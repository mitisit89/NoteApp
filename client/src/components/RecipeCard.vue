<template>
  <div class="card">
    <h1 class="card-title">{{ post.title }}</h1>
    <div class="card-content">
      <div class="content">{{ post.body }}</div>
    </div>
    <div class="card-footer">
      <b-button size="is-medium" type="is-danger" v-on:click="$emit('remove-item', post.id)">
        <span class="material-icons"> delete </span>
      </b-button>
      <router-link to='/edit'> <b-button size="is-medium"  type="is-warning">
           <span class="material-icons"> edit </span>
        </b-button> </router-link>
    </div>
  </div>
</template>
<script>
export default {
  props: {
    post: {
      type: Object,
      require: true,
    },
  },
};
</script>
<style scoped>
.card {
  display: inline-flex;
  flex-direction: column;
  justify-content: space-between;
  border: none;
  padding: 4rem 9rem;
  margin: 2% 2% 2%;
  border-radius: 10px;
  box-shadow: 0 0 5px;
  background: white;
}

.rm-btn {
  border-radius: 4%;
  margin: 10px 10px 10px;
  border: none;
  background: none;
}
h2 {
  text-decoration-line: underline;
}
.card-footer{
  justify-content: space-around;
}
</style>
