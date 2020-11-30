<template>
  <form @submit.prevent="onSubmint">
    <h2>Добавить</h2>
    <input type="text" v-model="title"/>
    <textarea v-model="body"></textarea>
    <button type="submit">Add</button>
  </form>
</template>
<script>
export default {
  data() {
    return {
      title: "",
      body:""
    };
  },
  methods: {
    onSubmint() {
      if (this.title.trim()) {
        const newObjectItem = {

          title: this.title,
          body:this.body,
        };
        this.$emit('add-item', newObjectItem)
      }
    }
  }
};
</script>

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

input {
  width: 400px;
}

button {
  margin-left: 1px;
}
</style>