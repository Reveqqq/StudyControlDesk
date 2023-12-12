<script>
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";

export default {
  name: 'Lesson',
  components: {FooterComp, HeaderComp },
  methods: {
    onAttendanceClick() {
      this.$router.push('/attendance')
    }
  }
}
</script>

<template>
<HeaderComp></HeaderComp>
  <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
  <img alt="star" class="star" src="../../public/images/star2.png">
  <div class="container">
    <h3 class="head">Предмет</h3>
    <p>Дата: 00.00.0000</p>
    <p>Пара №1</p>
    <p>Время: 8:30-10:00</p>
    <p>Группа: Б9122-01.03.02сп</p>
    <br>
    <button class="button">Отметить посещаемость</button>
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

p {
  font-family: MyriadaPro, serif;
  font-size: 29px;
}

.button {
  width: 250px;
  float: right;
  height: 35px;
  background-color: #b1d9ff;
  border: none;
  font-family: DelaGothicOne, serif;
  font-size: 15px;
  color: #4786c4;
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
  left: 0;
  top: 550px;
  z-index: -1;
}
</style>