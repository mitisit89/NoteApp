<template>
<div id="app">
    
    <Index />
</div>
</template>

<script>
import Index from "@/components/Index";

export default {
    name: "App",
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
