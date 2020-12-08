<template>
  <Form @add-item="addPost" />
</template>
<script>
import Form from "@/components/Form";
import { mapActions } from "vuex";
export default {
  components: {
    Form,
  },
  methods: 
    mapActions(['addPost']),
};
</script>