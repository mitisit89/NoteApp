export default {
  actions: {
    async authData() {
      const headers = { "Content-Type": "application/json;charset=utf-8" };
      const response = await fetch(
        "http://127.0.0.1:5000/api/getData",
        headers
      );
      if (response.ok) {
        const json = await response.json();
        Object.entries(json).map(([key, value]) => {
          localStorage.setItem(key, value);
        });
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
      }
    },
  },
  mutations: {
    updateComponent(state, isLogin) {
      state.keys = isLogin;
    },
  },
  state: {
    isLogin: "",
    token: localStorage.getItem("token") || "",
    user: [],
  },
  getters: {
    UserAuthData(state) {
      return state.user;
    },
  },
};
