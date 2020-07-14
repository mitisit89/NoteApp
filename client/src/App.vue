<template>
	<div id="app">
			<NavMenu/>
	<router-view />
	</div>
</template>
<script>
import NavMenu from '@/components/NavMenu'
export default {
	components:{
		NavMenu
	}
}
</script>

<style >
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
