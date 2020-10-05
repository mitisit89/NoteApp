<template>
  <div class="container">
    <h1>The Book of Recipe</h1>
    <Form @add-item="AddItem"/>
    <div class="row">
      <RecipeCard v-for="todo of todos" v-bind:todo="todo" :key="todo.id" v-on:remove-item="RemoveItem"/>
    </div>
  </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard";
import Form from "@/components/Form";
export default {
  components: {
    RecipeCard,
    Form,
  },
  data() {
    return {
      todos: [

      ]
    }
  },
  mounted() {
    fetch('http://127.0.0.1:5000/api/getData',{
      headers:{
        'Content-Type': 'application/json;charset=utf-8',
        'Allow':'http://10.0.1.9:8080/',
        
      }
    })
        .then(response => response.json())
        .then(json =>{this.todos=json})
  },
  methods: {
    RemoveItem(id) {
      console.log(id);
    this.todos=this.todos.filter(t => t.id !==id)

      fetch(`http://127.0.0.1:5000/api/delData/${id}`,{
        method:'DELETE'
      })
      },
    AddItem(item) {
      console.log(item);
      this.$emit("add-item", item);
      fetch('http://127.0.0.1:5000/api/postData',{
        method:'POST',
        headers:{'Content-Type': 'application/json;charset=utf-8'},
        body:JSON.stringify({title:item.title,body:'dsdsaadfa'})
      }).then(json=>console.log(json))
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  flex: 1;
  justify-content: space-around;
  position: relative;
  flex-direction: column;
  padding: 10px;
  margin: 10px;
  background-color: #8fabf2;
}

h1 {
  text-decoration: underline;
}

.row {
  display: flex;
  justify-content: space-around;
  position: relative;
  flex-direction:initial;
  padding: 0.5rem 2rem;
  margin-bottom: 1.5rem;
  align-content: stretch;
  align-items: baseline;
  flex-wrap: wrap;
}
</style>
