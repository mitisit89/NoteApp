import router from "@/router";
export default {
  actions: {
    async authLogin(context, data) {
      const headers = { "Content-Type": "application/json;charset=UTF-8" };
      const response = await fetch("http://127.0.0.1:5000/api/auth/login", {
        method: "POST",
        headers: headers,
        body: JSON.stringify(data),
      });
      if (response.ok) {
        const json = await response.json();

        router.push("/home");
        context.commit("loginStatus", json);
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
        ctx.commit()
        router.push("/login");
      }
    },
    async logout(context) {
      localStorage.clear();
      console.log("cleared");
      context.commit();
    },
  },
  mutations: {
    loginStatus(state, data) {
      for (const [key, value] of Object.entries(data)) {
        localStorage.setItem(`${key}`, value);
      }
      if (localStorage.getItem("token")) {
        return state.isLogin = "logged";
      }
    },
    
  },
  state: {
    isLogin: "",
    token: localStorage.getItem("token") || "",
    uID: localStorage.getItem("uid") || "",
  },
  getters: {
    getLoginStatus(state) {
      return state.isLogin;
    },
    getToken(state){
      return state.token;
    }
  },
};
