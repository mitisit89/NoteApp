<template>
  <div class="container">
    <div class="row">
      <RecipeCard
        v-for="post of getPosts"
        v-bind:post="post"
        :key="post.id"
        v-on:remove-item="removePost"
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
    this.fetchPosts();
  },
  methods: mapActions(["fetchPosts", "removePost"]),
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
  background-color:#BDBDBD;
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
