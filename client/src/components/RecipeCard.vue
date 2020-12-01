<template>
  <div class="card">
    <h2 class="card-title">{{ todo.title }}</h2>
    <div class="card-body">{{todo.body}}</div>
    <div class="meta">
      <span class="datetime">{{todo.time}}</span> <span class="tags">tags</span>
    </div>
    <button class="rm-btn" v-on:click="$emit('remove-item', todo.id)">
      <span class="material-icons"> delete </span>
    </button>
  </div>
</template>
<script>
export default {
  props: {
    todo: {
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
.material-icons:hover{
  color:red;
}

h2 {
  text-decoration-line: underline;
}
</style>
