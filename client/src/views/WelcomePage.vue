<template>
  <div class="container is-max-desktop">
    <h2 class="title is-2">Wellcome</h2>
    <b-tabs
      v-model="activeTab"
      position="is-centered"
      type="is-toggle"
      size="is-medium"
      class="block"
    >
      <b-tab-item label="login"> <Login /></b-tab-item>
      <b-tab-item label="Registration">
        <Registration />
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
import Login from "@/views/Login.vue";
import Registration from "@/views/Registration.vue";
export default {
  components: { Login, Registration },
  data() {
    return {
      activeTab: 0,
    };
  },
};
</script>

<style scoped>
</style>>
