<script setup>
import {ref, reactive} from 'vue';
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";

//TODO: запрос на API получить текущую дату + четность недели
const date = ref("11.12 (пн)");
const state = reactive ({
  allLessons: [
    {
      title: "Математический анализ (лек.)",
      groups: [
        "Б9122-01.03.02сп",
        "Б9122-01.03.02мкт",
        "Б9122-01.03.02сцт",
      ]
    },
    {
      title: "Математический анализ (прак.)",
      groups: [
        "Б9122-01.03.02сп",
      ]
    },
   ]
})


</script>

<template>
  <HeaderComp></HeaderComp>
  <div class="container">
    <h3 class="head">Мои занятия</h3>
    <p class="temp-week">Текущая неделя: 00 (чётная)</p>
    <table class="table">
      <tr >
        <td v-for="n in 7" :key="n">
            {{date}} <!--TODO: корректно реализовать заполнение даты-->
        </td>
      </tr>
    </table>
    <table>
      <tr 
      v-for="lessons in state.allLessons" 
      :key="lessons.id"
      >
        <td>
          <router-link
          v-for="title in lessons.title"
          :key="title.id"
          to="/lesson"
          class="lesson"
          >
          <a class="lesson">{{title}}</a>
          </router-link>
        </td>
        <td> <!--TODO: сделать не selector-ом -->
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