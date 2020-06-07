<template>
	<Index v-bind:objects="objects" @remove-item="RemoveItem" @add-item="AddItem" />
</template>
<script>
	import Index from "@/components/Index";

	export default {
		name: "App",
		data() {
			return {
				objects: []
			};
		},
		mounted() {
			fetch("https://jsonplaceholder.typicode.com/todos")
				.then(response => response.json())
				.then(json => {
					this.objects = json;
				});
		},
		methods: {
			RemoveItem(id) {
				this.objects = this.objects.filter(t => t.id !== id);
			},
			AddItem(item) {
				this.objects.push(item);
			}
		},
		components: {
			Index
		}
	};
</script>
<style>
@import url("https://fonts.googleapis.com/css?family=Ubuntu&display=swap&subset=cyrillic-ext");

* {
	box-sizing: border-box;
}

html,
body {
	font-family: "Ubuntu", sans-serif;
	background-color: #f1f5ff;
	margin: 0;
}

a {
	text-decoration: none;
}

li {
	list-style-type: none;
}
</style>
