<script>

import SideBar from "@/components/SideBar.vue";
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";

export default {
  name: 'AllLessons',
  components: {FooterComp, HeaderComp, SideBar },
  methods: {
    onLessonClick() {
      this.$router.push('/lesson')
    }
  }
}
</script>

<template>
  <HeaderComp></HeaderComp>
  <div class="container">
    <h4 class="head">Мои занятия</h4>
    <p class="temp-week">Текущая неделя: 00 (чётная)</p>
    <table class="table">
      <tr>
        <td><a href="#" class="days">00.00 (пн)</a></td>
        <td><a href="#" class="days">00.00 (вт)</a></td>
        <td><a href="#" class="days">00.00 (ср)</a></td>
        <td><a href="#" class="days">00.00 (чт)</a></td>
        <td><a href="#" class="days">00.00 (пт)</a></td>
        <td><a href="#" class="days">00.00 (сб)</a></td>
        <td><a href="#" class="days">00.00 (вс)</a></td>
      </tr>
    </table>
    <table>
      <tr>
        <td>
          <a class="lesson" href="#">Математический анализ (лек.)</a>
        </td>
        <td>
          <select class="selector">
          <option>Группа 1</option>
          <option>Группа 2</option>
          <option>Группа 3</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>
          <a class="lesson" href="#">Математический анализ (прак.)</a>
        </td>
        <td>
          <select class="selector">
          <option>Группа 1</option>
          <option>Группа 2</option>
          <option>Группа 3</option>
        </select>
        </td>
      </tr>
    </table>
  </div>
  <FooterComp></FooterComp>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 87vh;
  padding-top: 50px;
}

.head {
  font-family: "DelaGothicOne", serif;
  margin-bottom: 20px;
}

.table {
  table-layout: fixed;
  border-collapse: collapse;
  text-align: center;
  border-bottom: white;
}

.temp-week {
  font-family: "MyriadaPro", serif;
  font-size: 29px;
}

.days {
  margin-right: 45px;
  text-decoration: none;
  color: black;
  font-family: Inter, serif;
  font-weight: bold;
  font-size: 13px;
}

.lesson {
  font-family: "MyriadaPro", serif;
  font-size: 29px;
  text-decoration: none;
  color: black;
}

.selector {
  margin-left: 20px;
  font-family: Inter, serif;
  display: inline-block;
  border: none;
  padding: 5px;
}
</style>