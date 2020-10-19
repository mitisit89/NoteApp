<template>
  <Form @add-item="AddItem" />
</template>
<script>
import Form from "@/components/Form";
export default {
  components: {
    Form,
  },
  methods: {
    AddItem(item) {
      console.log(item);
      this.$emit("add-item", item);
      fetch("http://127.0.0.1:5000/api/postData", {
        method: "POST",
        headers: { "Content-Type": "application/json;charset=utf-8" },
        body: JSON.stringify(item),
      }).then((response)=>{
         if (response.ok){
             this.$router.push('/')
         }
      }).catch((e)=>{
          console.error(e);
      })
    },
  },
};
</script>