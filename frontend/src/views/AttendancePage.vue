<script setup>
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
import {ref, reactive} from 'vue'

const date = ref('11.12.2023');
const state = reactive({
  lessonData : {
  title: 'Математический анализ (лек.)',
  time: '8:30-10:00'
},
  students: [
    {
      FullName: 'Иван Иванов Иванович',
      group: 'Б9122-01.03.02сп',
      status: false
    },
    {
      FullName: 'Иван Иванов Игорьевич',
      group: 'Б9122-01.03.02мкт',
      status: false
    },
  ]  
})
</script>

<template>
  <HeaderComp></HeaderComp>
  <div class="container">
    <h3 class="head">{{state.lessonData.title}}</h3>
    <p class="date">{{date}}</p>
    <p class="date">{{state.lessonData.time}}</p>
    <div class="custom">
      <table class="table border-black">
        <thead>
        <tr>
          <th scope="col" class="number"></th>
          <th scope="col">Студент</th>
          <th scope="col">Номер группы</th>
          <th scope="col" class="define-border">Статус</th>
        </tr>
        </thead>
        <tr
        v-for="student in state.students"
        :key="student.id"
        >
          <td>{{ }}</td>
          <td>{{ student.FullName }}</td>
          <td>{{ student.group }}</td>
          <td class="define-border">+</td> <!--TODO: сделать чекбоксом-->
        </tr>
      </table>
    </div>
    <br>
    <router-link
        to="/qr"
        class="button1"
    >
    <button class="button1">Вывести QR-код</button>
    </router-link>
    <router-link
    to="/lessons"
    >
      <button class="button2">Проведена</button>
    </router-link>
    
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
  display: inline-block;
}

tr {
  text-align: center;
}

.date {
  display: inline-block;
  margin-left: 30px;
  font-family: MyriadaPro, serif;
  font-size: 25px;
}

.number {
  width: 5%;
}

.button1 {
  width: 250px;
  height: 35px;
  background-color: #ABDCFF;
  border: none;
  font-family: DelaGothicOne, serif;
  font-size: 15px;
  color: #2B75B9;
}

.button2 {
  width: 250px;
  float: right;
  height: 35px;
  background-color: #ABDCFF;
  border: none;
  font-family: DelaGothicOne, serif;
  font-size: 15px;
  color: #2B75B9;
}
</style>