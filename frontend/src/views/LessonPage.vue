<script setup>
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
import {lesson_id} from "@/../static/state"
import {ref, reactive, onMounted} from 'vue';

const date = ref('20.12.2023');
const state = reactive({
  lessonData : {
  // title: 'Математический анализ (лек.)',
  // num: '№1',
  // time: '8:30-10:00', 
  // groups: [
  //   'Б9122-01.03.02сп'
  // ]
}
})


onMounted(() => {
  fetch(process.env.VUE_APP_API_URL + '/lesson/' + lesson_id.id, {
    method: 'GET',
    headers : {
       Authorization: 'Bearer ' + localStorage.getItem('token'),
    }
  })
      .then(response => response.json())
      .then(data => {
        state.lessonData = data
        console.log(data);
      }).catch(error => {
    console.error(error);    // Обработка ошибки
  });
})
</script>

<template>
<HeaderComp></HeaderComp>
  <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
  <img alt="star" class="star" src="../../public/images/star2.png">
  <div class="container">
    <h3 class="head">{{ state.lessonData.title }}</h3>
    <p>Дата: {{ date }}</p>
    <p>Пара {{ state.lessonData.num }}</p>
    <p>Время: {{ state.lessonData.time }}</p>
    <p
    v-for="(group, index) in state.lessonData.groups"
    :key="index"
    >
    Группы: {{ group }}</p>
    <br>
    <router-link
        to="/attendance"
        class="button"
    >
      <button class="button">Отметить посещаемость</button>
    </router-link>
  </div>
  <FooterComp class="footer"></FooterComp>
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
  background-color: #ABDCFF;
  border: none;
  font-family: DelaGothicOne, serif;
  font-size: 15px;
  color: #2B75B9;
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
  bottom: -100px;
  z-index: -1;
}

@media (max-width: 1350px) {
  .footer {
    display: none;
  }
}

@media (max-width: 500px) {
  .ellipse {
    display: none;
  }
  .star {
    display: none;
  }
}
</style>