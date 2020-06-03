<template>
	<form @submit.prevent="onSubmint">
		<input type="text" v-model="title" />
		<button type="submit">Add</button>
	</form>
</template>
<script>
	export default {
		data() {
			return {
				title: ""
			};
		},
		methods: {
			onSubmint() {
				console.log("on", this.title);
				if (this.title.trim()) {
					const newObjectItem = {
                        id: Date.now(),
                        title:this.title
                    };
                    this.$emit('add-item', newObjectItem )
				}
			}
		}
	};
</script>

<style  scoped>
form {
	display: flex;
}
input {
	width: 400px;
}
button {
	margin-left: 1px;
}
</style>