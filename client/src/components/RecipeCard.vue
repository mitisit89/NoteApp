<template>
	<div class="card">
		<h1>{{ item.id }}</h1>
		<div class="card-body">{{ item.title }}</div>
		<span class="datetime">datetime</span>
		<span class="tags">tags</span>
		<button class="rm-btn" v-on:click="$emit('remove-item', item.id)">
			&times;
		</button>
	</div>
</template>
<script>
	export default {
		props: {
			item: {
				type: Object,
				require: true
			}
		}
	};
</script>
<style scoped>
	.card {
		border: 1px solid black;
		padding: 1%;
		margin-top: 2%;
	}
	.rm-bnt {
		border-radius: 50%;
	}
</style>
