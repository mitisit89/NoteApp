<template>
  <RegForm @add-new-user="authRegistration"/>
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
