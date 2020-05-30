<template>
	<div class="conteiner">
		<hedear>
			<NavMenu />
		</hedear>

		<h1>The Book of Recipe</h1>
		<hr />
		<div class="row">
			<RecipeCard />
		</div>
	</div>
</template>

<script>
	import RecipeCard from "@/components/RecipeCard";
	import NavMenu from "@/components/NavMenu";
	export default {
		components: {
			RecipeCard,
			NavMenu
		}
	};
</script>

<style scoped>
.container {
	display: flex;
	flex: 1;
	justify-content: space-around;
	position: relative;
	flex-direction: column;
	padding: 10px;
	margin: 10px;
	background-color: #8fabf2;
}
.row {
	display: flex;
	flex: 1;
	justify-content: space-around;
	position: relative;
	flex-direction: column;
	padding: 10px;
	margin: 10px;
	background-color: #8fabf2;
}
</style>