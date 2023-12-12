<script>
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";

export default {
  name: 'AllLessons',
  components: {FooterComp, HeaderComp },
  methods: {
    onLessonClick() {
      this.$router.push('/lesson')
    }
  }
}
</script>

<template>
  <HeaderComp></HeaderComp>
  <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
  <img alt="star" class="star" src="../../public/images/star.png">
  <div class="container">
    <h3 class="head">Мои занятия</h3>
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
          <a class="lesson" href="#" @click.prevent="onLessonClick()">Математический анализ (лек.)</a>
        </td>
        <td>
          <select class="selector">
          <option class="option_head" selected disabled label="Группы"></option>
          <option disabled="disabled">Б9122-01.03.02сп</option>
          <option disabled="disabled">Б9122-01.03.02мкт</option>
          <option disabled="disabled">Б9122-01.03.02сцт</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>
          <a class="lesson" href="#" @click.prevent="onLessonClick()">Математический анализ (прак.)</a>
        </td>
        <td>
          <select class="selector">
            <option class="option_head" selected disabled label="Группы"></option>
            <option disabled="disabled">Б9122-01.03.02сп</option>
            <option disabled="disabled">Б9122-01.03.02мкт</option>
            <option disabled="disabled">Б9122-01.03.02сцт</option>
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

option:disabled {
  color: black;
  font-family: Inter, serif;
  font-weight: bold;
}

.head {
  font-family: "DelaGothicOne", serif;
  margin-bottom: 20px;
}

.option_head {
  text-align: center;
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
  padding-top: 5px;
  padding-bottom: 5px;
  user-focus: none;
  user-select: none;
}

.ellipse {
  position: absolute;
  top: 270px;
  width: 85px;
  right: 0;
  z-index: -1;
}

.star {
  position: absolute;
  width: 150px;
  top: 610px;
  z-index: -1;
  right: 0;
}
</style>