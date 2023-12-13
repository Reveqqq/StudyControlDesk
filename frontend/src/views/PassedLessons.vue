<script setup>
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
import {reactive} from 'vue';

const state = reactive ({
  passedLessons: [
    {
      title: "Математический анализ (лек.)",
      groups: [
        "Б9122-01.03.02сп",
        "Б9122-01.03.02мкт",
        "Б9122-01.03.02сцт",
      ],
      conducted: false, //статус что пара проведена
      date: '13.12.2023'
    },
    {
      title: "Математический кекс (прак.)",
      groups: [
        "Б9122-01.03.02сп"
        
      ],
      conducted: false,
      date: '14.12.2023'
    },
   ]
})

</script>

<template>
  <HeaderComp></HeaderComp>
  <div class="container">
    <h3 class="head">Список проведённых занятий</h3>
    <div class="custom">
      <table class="table border-black">
        <thead>
        <tr>
          <th scope="col">Предмет</th>
          <th scope="col">Дата</th>
          <th scope="col">Номер группы</th>
          <th scope="col" class="define-border">Редактировать</th>
        </tr>
        </thead>
        <tr
        v-for="lesson in state.passedLessons"
        :key="lesson.id"
        >
          <td>{{lesson.title}}</td>
          <td>{{lesson.date}}</td>
          <td>
            <div
            style="padding: 1%; margin: 1%;"
            v-for="group in lesson.groups"
            :key="group.id"
            >
              {{ group }}
            </div>
          </td>
          <td class="define-border">
            <a href="#">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
              <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
              <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
              </svg>
            </a>
          </td>
        </tr>
      </table>
    </div>
  </div>
  <FooterComp></FooterComp>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 87vh;
  padding-top: 50px;
}

a {
  color: black;
}

.table {
  table-layout: fixed;
  border-collapse: collapse;
}

th {
  font-family: "MyriadaPro", serif;
  font-size: 20px;
  font-weight: normal;
  border: 1px solid black;
  border-left: none;
  border-top: none;
}

td {
  border: 1px solid black;
  border-left: none;
  font-family: "Inter", serif;
  color: black;
}

.define-border {
  border-right: none;
}

.custom {
  border: 2px solid black;
  border-radius: 15px;
  overflow: hidden;
}

.head {
  font-family: "DelaGothicOne", serif;
  margin-bottom: 30px;
}

tr {
  text-align: center;
}
</style>