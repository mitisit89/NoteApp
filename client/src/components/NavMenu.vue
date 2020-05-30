<template>
	<nav class="navigation">
		<div class="nav-menu">
			<ul class="nav-list">
				<li class="nav-link">
					<a href>Главая</a>
				</li>

				<li class="nav-link">
					<a href="#">Lorem3</a>
				</li>

				<li class="nav-link">
					<a href="#">Lorem4</a>
				</li>
				<li class="nav-link">
					<a href="#">Admin</a>
				</li>

				<li class="nav-link">
					<a href="#">Создать запись</a>
				</li>
				<li class="nav-link">
					<a href="#">Выход</a>
				</li>
				<li class="nav-link">
					<a href="#">Вход</a>
				</li>
				<li class="nav-link">
					<a href="#">Регистрация</a>
				</li>
			</ul>
		</div>
	</nav>
</template>

<script>
	export default {};
</script>

<style>
.navigation {
	display: flex;
	flex-flow: row;
	background-color: #3d3d3f;
	color: white;
	padding: 10px;
	margin: 10px;
	position: relative;
	align-content: space-between;
}
.nav-list,
.auth-list {
	display: inline-flex;
}

.nav-link {
	flex-flow: row wrap;
	padding: inherit;
}
.nav-link a {
	color: white;
}
.nav-menu{
display:flex;
align-content: inherit;
  align-content: space-between;
}

</style>