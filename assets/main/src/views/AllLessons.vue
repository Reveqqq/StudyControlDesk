<script>

import SideBar from "@/components/SideBar.vue";

export default {
  name: 'AllLessons',
  components: { SideBar },
  methods: {
    onLessonClick() {
      this.$router.push('/lesson')
    }
  }
}
</script>

<template>
  <div style="width: 100vw; height: 100vh; position: relative">
    <SideBar></SideBar>
    <div style="height: 100vh; display: inline-block; position: absolute; width: 80vw">
      <h2 style="text-align: center; font-weight: bold;">Список занятий</h2><br><br>
      <a href="#" @click.prevent="onLessonClick()" style="margin-left: 40px; margin-top: 100px">Математический анализ</a><br>
      <a style="margin-left: 40px;">Углубленные вопросы математического анализа</a>
    </div>
  </div>
</template>

<style scoped>
h2 {
  font-family: 'Ubantu', sans-serif;
  font-style: italic;
  margin-top: 45px;
}

a {
  font-size: 1.2em;
}

body {
  width: 100%;
  height: 100vh;
  margin: 0;
  overflow: hidden;
  font-family: 'Ubantu', sans-serif;
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