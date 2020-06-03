<template>
	<div class="conteiner">
		<header>
			<NavMenu />
		</header>

		<h1>The Book of Recipe</h1>
		<Form @add-item='AddItem'/>
		<div class="row">
			<!-- eslint-disable-next-line-->
			<RecipeCard
				v-for="item in objects"
				v-bind:item="item"
				v-on:remove-item="RemoveItem"
			/>
		</div>
	</div>
</template>

<script>
	import RecipeCard from "@/components/RecipeCard";
	import NavMenu from "@/components/NavMenu";
	import Form from "@/components/Form";
	export default {
		props: ["objects"],
		components: {
			RecipeCard,
			NavMenu,
			Form
		},
		methods: {
			RemoveItem(id) {
				console.log(id);
				this.$emit("remove-item", id);
			},
			AddItem(item){
				console.log(item);
				this.$emit("add-item",item)
			}
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
	h1 {
		text-decoration: underline;
	}
	.row {
		display: flex;
		justify-content: space-evenly;
		position: relative;
		flex-direction: inherit;
		padding: 0.5rem 2rem;
		margin-bottom: 1.5rem;
		align-content: stretch;
		align-items: baseline;
		flex-wrap: wrap;
	}
</style>
