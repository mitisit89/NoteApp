export default {
    actions: {
        async fetchPosts(context) {
            const headers = {
                "Content-Type": "application/json;charset=utf-8",
                Allow: "http://10.0.1.9:8080/",
            }
            const response = await fetch("http://127.0.0.1:5000/api/getData", headers)
            const posts = await response.json()
            context.commit('update', posts)
        }
    },
    mutations: {
        update(state, posts) {
            state.posts = posts

        }
    },
    state: {
        posts: []
    },
    getters: {
        getPosts(state) {
            return state.posts
        }
    }
}