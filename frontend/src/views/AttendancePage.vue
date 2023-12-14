<script setup>
import HeaderComp from "@/components/HeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
import {ref, reactive, watch} from 'vue'

const date = ref('11.12.2023');
const status = ref(false);
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

watch(status, (newStatus) =>{
  state.students.forEach(student => {
    student.status = newStatus
  });
})

</script>

<template>
  <HeaderComp></HeaderComp>
  <div class="container">
    <h3 class="head">{{state.lessonData.title}}</h3>
    <p class="date">{{date}}</p>
    <p class="date">{{state.lessonData.time}}</p>
    <p class="date">Отметить всех: 
      <input v-model="status" type="checkbox">
    </p>  
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
        v-for="(student, index) in state.students"
        :key="index"
        >
          <td>{{ index + 1 }}</td>
          <td>{{ student.FullName }}</td>
          <td>{{ student.group }}</td>
          <td class="define-border"><input v-model="student.status" type="checkbox"></td>
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
  <FooterComp class="footer"></FooterComp>
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
  padding: 5px;
}

td {
  border: 1px solid black;
  border-left: none;
  font-family: "Inter", serif;
  color: black;
  padding: 5px;
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
  width: 40px;
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

input[type="checkbox"] {
  appearance: none;
  display: grid;
  place-content: center;
  margin: 0 auto;
  border: 1px solid black;
  width: 1em;
  height: 1em;
}

input[type="checkbox"]::before {
  content: "";
  transform: scale(0);
  width: 0.8em;
  height: 0.8em;
  transition: 120ms transform ease-in-out;
  box-shadow: inset 1em 1em black;
  transform-origin: bottom left;
  clip-path: polygon(14% 44%, 0 65%, 50% 100%, 100% 16%, 80% 0%, 43% 62%);
}

input[type="checkbox"]:checked::before {
  transform: scale(1);
}

@media (max-width: 1350px) {
  .footer {
    display: none;
  }
}

@media (max-width: 1000px) {
  .head {
    display: block;
  }

  .date {
    display: inline-block;
    margin-left: 0;
    margin-right: 30px;
  }
}

@media (max-width: 550px) {
  .button1, .button2 {
    width: 120px;
    font-size: 10px;
    margin-bottom: 10px;
  }

  th {
    font-size: 17px;
  }

  td {
    font-size: 12px;
  }

  .date {
    font-size: 20px;
  }
}
</style>