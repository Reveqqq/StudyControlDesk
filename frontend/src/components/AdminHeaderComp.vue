<script setup>
function Exit(){
  localStorage.clear();
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
        <router-link
            to="/"
            class="exit"
        >
          <a @click="Exit()" href="#" class="exit">Выйти</a>
        </router-link>
      </div>
    </div>
    <nav class="nav">
      <router-link
          class="links"
          to="/passed_lessons"
      >
        <a href="#" class="links">Студенты</a>
      </router-link>
      <router-link
          class="links"
          to="/groups"
      >
        <a href="#" class="links">Группы</a>
      </router-link>
      <router-link
          class="links"
          to="/teachers"
      >
        <a href="#" class="links">Преподаватели</a>
      </router-link>
      <router-link
          class="links"
          to="/lessons"
      >
        <a href="#" class="links">Предметы</a>
      </router-link>
      <router-link
          class="links"
          to="/programs"
      >
        <a href="#" class="links">Образовательные программы</a>
      </router-link>
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
  margin-right: 10px;
  margin-left: 10px;
  margin-top: 30px;
  text-decoration: none;
  color: black;
  font-family: "Inter", serif;
  font-weight: bold;
  text-align: center;
  font-size: 1em;
}

.nav {
  width: 100vw;
  height: 5vh;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-top: 10px;
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

@media (max-width: 768px) {
  .image-logo {
    display: none;
  }

  .links {
    font-size: 0.9em;
  }

  .image-search {
    width: 25px;
  }

  .exit {
    margin-left: 10px;
  }
}

@media (max-width: 350px) {
  .links {
    font-size: 0.8em;
  }
}
</style>