<template>
 <RegForm @addNewUser='authRegistration' />
</template>

<style scoped>

</style>
<script>
import { mapActions } from "vuex";
import RegForm from '../components/RegForm';
export default {
  componets:{
    RegForm
  },
  methods: mapActions(["authRegistration"]),

};
</script>
