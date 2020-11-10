<template>
  <div class="container">
    <h1>The Book of Recipe</h1>
    <div class="row">
      <RecipeCard
        v-for="todo of getPosts"
        v-bind:todo="todo"
        :key="todo.id"
        v-on:remove-item="RemoveItem"
      />
    </div>
  </div>
</template>

<script>
import RecipeCard from "@/components/RecipeCard";
import { mapGetters, mapActions } from "vuex";
export default {
  components: {
    RecipeCard,
  },
  computed: mapGetters(["getPosts"]),
  async mounted() {
    this.fetchPosts()
  },
  methods: 
    mapActions(['fetchPosts']),
    RemoveItem(id) {
      console.log(id);
      this.todos = this.todos.filter((t) => t.id !== id);

      fetch(`http://127.0.0.1:5000/api/delData/${id}`, {
        method: "DELETE",
      });
    },
  
};
</script>

<style scoped>
.container {
  display: flex;
  flex: 1;
  max-width: 1440px;
  margin: 0px auto;
  padding: 0px 15px;
  z-index: 1;
  padding-top: 1rem;
  justify-content: space-around;
  position: relative;
  flex-direction: column;
  background-color: #8fabf2;
}

h1 {
  text-decoration: underline;
}

.row {
  display: flex;
  justify-content: space-around;
  position: relative;
  flex-direction: initial;
  padding: 0.5rem 2rem;
  margin-bottom: 1.5rem;
  align-content: stretch;
  align-items: baseline;
  flex-wrap: wrap;
}
@media (max-width: 1400px) {
  .container,
  #navigaton {
    max-width: 970px;
  }
}
@media (max-width: 992px) {
  .container,
  #navigaton {
    max-width: 750px;
  }
}
@media (max-width: 767px) {
  .container,
  #navigaton {
    max-width: none;
  }
}
</style>
