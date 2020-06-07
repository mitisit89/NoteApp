<template>
	<div class="card">
		<h2>{{ item.id }}</h2>
		<div class="card-body">{{ item.title }}</div>
		<div class="meta"><span class="datetime">datetime</span>
		<span class="tags">tags</span></div>
		
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
		display: inline-flex;
		flex-direction: column;
		justify-content:  space-between;
		border: 1px solid black;
		padding: 1.25rem;
		margin-top: 2%;
		
	}
	.rm-btn {
		border-radius: 40%;
		padding: 1rem;
		width: 10px;
		top: 0;
		right: 0;
		position: static;

	}
	h2{
		text-decoration-line: underline;
	}
</style>
