import router from "@/router";
export default {
  actions: {
    async fetchPosts(context) {
      const headers = {
        "Content-Type": "application/json;charset=utf-8",
        Authorization: `Bearer ${localStorage.getItem("token")}`,
      };
      const response = await fetch("http://127.0.0.1:5000/api/getData", {
        method: "Get",
        headers: headers,
      });
      const posts = await response.json();
      console.log(posts);
      context.commit("update", posts);
    },
    async addPost(context, post) {
      console.log(post);
      const response = await fetch("http://127.0.0.1:5000/api/postData", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=utf-8",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify(post),
      });
      if (response.ok) {
        context.commit("update", post);
        router.push("/home");
      }
    },
    async removePost(context, id) {
      console.log(id);
      const response = await fetch(`http://127.0.0.1:5000/api/delData/${id}`, {
        method: "DELETE",
        headers:{
        Authorization: `Bearer ${localStorage.getItem("token")}`,}
      });
      if (response.ok) {
        console.log("ok");
        context.commit("remove", id);
      }
    },
    async editPost(context,editedPost){
      const response = await fetch('http://127.0.0.1:5000/api/postUpdate/',{
        method:'PUT',
        headers:{
          Authorization: `Bearer ${localStorage.getItem("token")}`
        },
          body:JSON.stringify(editedPost)
        });
        if(response.ok){
          context.commit('update')
        }
    }
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
