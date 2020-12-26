<template>
    <form @submit.prevent="onSubmint">
        <b-field label="Name">
            <b-input v-model="name"></b-input>
        </b-field>

        <b-field label="Email"
            type="is-danger"
            message="This email is invalid">
            <b-input type="email"
                v-model="email"
                maxlength="30">
            </b-input>
        </b-field>
        <b-field label="Username">
            <b-input
            ></b-input>
        </b-field>
        <b-field label="Password">
            <b-input type="password"
                v-model="password"
                password-reveal>
            </b-input>
            <p>Hell</p>
        </b-field>
    </form>
</template>

<script>
export default{
    el:'b-field ',
    data(){
        return{
            email:"",
            username:"",
            password:""
        }
    },
    methods:{onSubmint(){
       const newUser={
           email:this.email,
           username:this.username,
           password:this.password
       }
       this.$emit('addNewUser',newUser)
    }}
    
}


</script>