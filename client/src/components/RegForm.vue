<template>
    <form @submit.prevent="onSub">
        <b-field label="Email"
            type="is-danger"
            message="This email is invalid">
            <b-input type="email"
                v-model="email"
                maxlength="30" />
        </b-field>
        <b-field label="Username">
            <b-input
            v-model="username"
            />
        </b-field>
        <b-field label="Password">
            <b-input type="password"
                v-model="password"
                password-reveal>
            </b-input>
            <p>Hell</p>
        </b-field>
   <b-button class="button is-primary">Search</b-button>
   </form>
</template>

<script>
export default {
    data(){
        return{
            email:'',
            username:'',
            password:''
        }
    },
    methods:{
        onSub(){
            const newUser={
                email:this.email,
            username:this.username,
            password:this.password
            }
            this.$emit('add-new-user',newUser)
        }
    }
}
</script>