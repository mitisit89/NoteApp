import router from "@/router";
export default {
  actions: {
    async fetchPosts(context) {
      const headers = {
        "Content-Type": "application/json;charset=utf-8",
        Allow: "http://10.0.1.9:8080/",
      };
      const response = await fetch(
        "http://127.0.0.1:5000/api/getData",
        headers
      );
      const posts = await response.json();
      context.commit("update", posts);
    },
    async addPost(context, post) {
      console.log(post);
      const response = await fetch("http://127.0.0.1:5000/api/postData", {
        method: "POST",
        headers: { "Content-Type": "application/json;charset=utf-8" },
        body: JSON.stringify(post),
      });
      if(response.ok){
        router.push('/')
      
      context.commit()}
   
    },
    async removePost(context, id) {
      console.log(id);
      const response = await fetch(`http://127.0.0.1:5000/api/delData/${id}`, {
        method: "DELETE",
      });
      if (response.ok) {
        console.log("ok");
        context.commit("remove", id);
      }
    },
  },
  mutations: {
    update(state, posts) {
      state.posts = posts;
    },
    remove(state, id) {
      state.posts = state.posts.filter((todo) => todo.id !== id); // метод filter возвращает новый массив
    },
  },
  state: {
    posts: [],
  },
  getters: {
    getPosts(state) {
      return state.posts;
    },
  },
};
