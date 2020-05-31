<template >
	<div class="card">
		<h1>{{item.id}}</h1>
		<div class="card-body">{{item.title }}</div>
		<span class="datetime">datetime</span>
		<span class="tags">tags</span>
	</div>
</template>
<script>
export default {
	props:{
		item:{
			type:Object,
			require:true
		}
	}
}
</script>
<style scoped>
.card{
	border: 1px solid black;
	padding: 1%;
}
</style>
