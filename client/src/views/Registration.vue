<template>
  <RegForm />
</template>

<script>
import RegForm from '@/components/RegForm';
import { mapActions } from "vuex";

export default {
  components:{
    RegForm,
  },
  methods: mapActions(["authRegistration"]),

};
</script>
