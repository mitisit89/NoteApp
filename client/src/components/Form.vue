<template>
  <div class="container">
  <form @submit.prevent="onSubmint" class="box" position="is-centered" size='is-medium'>
     <b-field label="Title">
    <b-input type="text"  v-model="title" /></b-field>
    <b-field label='Text'>
    <b-input type='textarea' v-model="body"></b-input></b-field>
    <b-button type="is-success" native-type=submit >Add</b-button>
  </form></div>
</template>
<script>
export default {
  props:['formTitle'],
  data() {
    return {
      title: "",
      body: "",
    };
  },
  methods: {
    onSubmint() {
      if (this.title.trim()) {
        const newObjectItem = {
          title: this.title,
          body: this.body,
        };
        this.$emit("add-item", newObjectItem);
      }
    },
  },
};
</script>

