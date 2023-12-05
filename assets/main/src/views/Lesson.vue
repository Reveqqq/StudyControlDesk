<script>
import SideBar from "@/components/SideBar.vue";

export default {
  name: 'Lesson',
  components: { SideBar },
  methods: {
    onAttendanceClick() {
      this.$router.push('/attendance')
    }
  }
}
</script>

<template>
  <div style="width: 100vw; height: 100vh; position: relative">
    <SideBar></SideBar>
    <div style="height: 100vh; display: inline-block; position: absolute; width: 80vw">
      <div style="height: 75vh">
        <h2 style="text-align: center; font-weight: bold">Математический анализ (прак.)</h2>
        <p style="margin-left: 40px; margin-top: 80px">Дата: 01.01.2023</p><br>
        <p style="margin-left: 40px;">Время: 16:50-18:20</p><br>
        <p style="margin-left: 40px;">Группы:</p>
        <ul>
          <li><a href="#">Б9122 01.03.02сп</a></li>
          <li><a href="#">Добавить группу</a></li>
        </ul>
          <a style="margin-left: 40px; margin-top: 50px" @click.prevent=onAttendanceClick() href="#" class="btn btn-primary btn active" role="button" aria-pressed="true">Отметить</a>
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