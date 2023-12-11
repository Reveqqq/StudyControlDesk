<script>

export default {
  name: 'HeaderComp'
}
</script>

<template>
<header>
  <div class="header">
    <div class="left">
      <img alt="logo" class="image-logo" src="../../public/images/logo_department.png">
    </div>
    <div class="right">
      <a href="#"><img alt="search" class="image-search" src="../../public/images/search_button.png"></a>
      <a href="#" class="exit">Выйти</a>
    </div>
  </div>
  <nav class="nav">
    <a href="#" class="links">Список проведённых занятий</a>
    <a href="#" class="links">Мои занятия</a>
  </nav>
</header>
</template>

<style scoped>

.header {
  width: 100vw;
  height: 8vh;
  padding: 20px;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}

.links {
  padding: 20px;
  text-decoration: none;
  color: black;
  font-family: "Inter", serif;
  font-weight: bold;
  text-align: center;
  font-size: 15px;
}

.nav {
  width: 100vw;
  height: 5vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.left {
  width: 50vw;
  height: 8vh;
}

.image-logo {
  width: 300px;
}

.image-search {
  display: inline-block;
  width: 30px;
}

.exit {
  display: inline-block;
  margin-left: 20px;
  color: #b7b7b7;
  font-family: "MyriadaPro", serif;
  font-size: 20px;
  text-decoration: none;
}

.right {
  display: inline-block;
  width: 50vw;
  text-align: right;
  height: 8vh;
}

</style>