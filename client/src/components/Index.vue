<template>
	<div class="conteiner">
		<header>
			<NavMenu />
		</header>

		<h1>The Book of Recipe</h1>
		<hr />
		<div class="row">
			<!-- eslint-disable-next-line-->
			<RecipeCard v-for="item in objects" :item="item" />
		</div>
	</div>
</template>

<script>
	import RecipeCard from "@/components/RecipeCard";
	import NavMenu from "@/components/NavMenu";
	export default {
		props: ["objects"],
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
		justify-content:space-evenly;
		position: relative;
		flex-direction: inherit;
		padding: 10px;
		margin: 10px;
		align-content: stretch;
		align-items: baseline;
	
	}
</style>
