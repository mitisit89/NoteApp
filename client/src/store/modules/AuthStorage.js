export default {
  actions: {
    async authLogin(context, data) {
      const headers = { "Content-Type": "application/json;charset=utf-8" };
      const body = JSON.stringify(data);
      const response = await fetch("http://127.0.0.1:5000/api/auth/login", {
        method: "POST",
        headers: headers,
        body: body,
      });
      if (response.ok) {
        const json = await response.json()
        for (const [key,value] of Object.entries(json)) {
          localStorage.setItem(`${key}`,value)
        }
        this.$router.push('/')
        context.commit('loginStatus',localStorage.getItem("token"))
      }
    },
    async authRegistration(ctx, data) {
      console.log(data);
      const headers = { "Content-Type": "application/json;charset=utf-8" };
      const response = await fetch(
        "http://127.0.0.1:5000/api/auth/registration",
        {
          method: "POST",
          headers: headers,
          body: JSON.stringify(data),
        }
      );
      if (response.ok) {
        console.log("ok");
        this.$router.push('/login')
      }
    },async logout(context){
      localStorage.clear()
      console.log('cleared');
      context.commit('refreshVeux')
     }
  },
  mutations: {
    loginStatus(state,token){
      state.isLogin='logged',
      state.token=token
    }
        
    },
  state: {
    isLogin:'',
    token: localStorage.getItem("token") || "",
    uID:localStorage.getItem("uid") || "",
  },
  getters: {
    getIslogin(state){
      return state.isLogin
    }
  },
};
