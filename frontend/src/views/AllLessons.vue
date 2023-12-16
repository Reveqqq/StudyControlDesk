<script setup>
import {ref, reactive, onMounted} from 'vue';
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
import {ChangeId} from "@/../static/state"

onMounted(() => {
  fetch(process.env.VUE_APP_API_URL + '/lessons/my/', {
    method: 'GET',
    headers : {
       Authorization: 'Bearer ' + localStorage.getItem('token'),
    }
  })
      .then(response => response.json())
      .then(data => {
        state.allLessons = data
        console.log(data);
      }).catch(error => {
    console.error(error);    // Обработка ошибки
  });
})

const week = ref(9)
const date = ref('18.12.2023');
const days = [
  '(пн)',
  '(вт)',
  '(ср)',
  '(чт)',
  '(пт)',
  '(сб)',
  '(вс)'
];
var day = date.value.split('.')[0]
var month = date.value.split('.')[1]
// var year = date.value.split('.')[2]
const state = reactive ({
  allLessons: [
    // {
    //   title: "Математический анализ (лек.)",
    //   groups: [
    //     "Б9122-01.03.02сп",
    //     "Б9122-01.03.02мкт",
    //     "Б9122-01.03.02сцт",
    //   ],
    //   conducted: false,
    //   id : 1
    // },
   ]
})


</script>

<template>
  <HeaderComp></HeaderComp>
  <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
  <img alt="star" class="star" src="../../public/images/star.png">
  <div class="container">
    <h3 class="head">Мои занятия</h3>
    <p class="temp-week">Текущая неделя: {{week}} {{week % 2 == 0 ? '(чётная)' : '(нечётная)'}}</p>
    <table class="table">
      <tr > 
        <td v-for="n in 7" :key="n" class="days">
            {{ parseInt(day) + n - 1 + '.' + month + days[n-1]}}
        </td>
      </tr>
    </table>
    <table>
      <tr
      v-for="lesson in state.allLessons"
      :key="lesson.id"
      >
        <td>
          <router-link
          v-for="(title, index) in lesson.title"
          :key="index"
          to='/lesson'
          class="lesson"
          >
          <a @click="ChangeId(lesson.id)" class="lesson">{{title}}</a>
          </router-link>
        </td>
        <td>  
          <select class="selector">
          <option class="option_head" selected disabled>Группа</option>
          <option 
          disabled="disabled" 
          v-for="group in lesson.groups"
          :key="group.id"
          >
          {{ group }}
          </option>
          </select>
        </td>
      </tr>
    </table>
  </div>
  <FooterComp class="footer"></FooterComp>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 87vh;
  padding-top: 50px;
}

.option_head {
  text-align: center;
  font-family: Inter, serif;
  font-weight: bold;
}

option:disabled {
  font-family: Inter, serif;
  font-weight: bold;
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
  padding-top: 5px;
  padding-bottom: 5px;
  width: 160px;
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
  right: 0;
  z-index: -1;
  width: 150px;
  top: 83%;
}

@media (max-width: 1350px) {
  .footer {
    display: none;
  }
}

@media (max-width: 620px) {
  .ellipse {
    display: none;
  }
  .star {
    display: none;
  }
}

@media (max-width: 500px) {
  .table {
    display: none;
  }

  .lesson {
    font-size: 20px;
  }
}
</style>