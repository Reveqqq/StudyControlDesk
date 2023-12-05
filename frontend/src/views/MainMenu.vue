<script>

import SideBar from "../components/SideBar.vue";

export default {
  name: 'MainMenu',
  components: { SideBar }
};

</script>

<template>
  <div style="width: 100vw; height: 100vh; position: relative">
  <SideBar></SideBar>
    <div style="height: 100vh; display: inline-block; position: absolute; width: 80vw">
      <h2 style="text-align: center; font-weight: bold">Новости</h2>
      <div style="height: 30vh; width: 81vw; margin-top: 50px">
        <div style="height: 100%; width: 30vw; display: inline-block; margin-left: 30px">
          Блок для картинки
        </div>
        <div style="height: 100%; width: 40vw; display: inline-block;">
          Блок для текста
        </div>
        <div style="height: 1px; background-color: lightgrey"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h2 {
  font-family: 'Ubantu', sans-serif;
  font-style: italic;
  margin-top: 45px;
}

body {
  width: 100%;
  height: 100vh;
  margin: 0;
  overflow: hidden;
  font-family: 'Ubantu', sans-serif;
}

p {
  font-size: 1.2em;
}

li {
  list-style-type: none;
  padding: 5px;
  margin: 5px;
  width: 200px;
  font-size: 1.2em;
  white-space: nowrap
}
</style>