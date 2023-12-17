<script setup>

import AdminHeaderComp from "@/components/AdminHeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
</script>

<template>
  <AdminHeaderComp></AdminHeaderComp>
  <div class="container">
    <h3 class="head">Преподаватели</h3>
    <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
    <div class="custom">
      <table class="table border-black">
        <thead>
        <tr>
          <th scope="col">ФИО</th>
          <th scope="col">Школа/институт</th>
          <th scope="col">E-mail</th>
          <th scope="col" class="define-border">Редактировать</th>
        </tr>
        </thead>
        <tr>
          <td>Зиновьев Павел Владимирович</td>
          <td>Политехнический институт</td>
          <td>zinovev.pv@dvfu.ru</td>
          <td class="define-border">
            <a href="#">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
              </svg>
            </a></td>
        </tr>
      </table>
    </div>
    <br>
    <router-link
        to="/add_teacher"
    >
      <button type="submit" class="button">Добавить преподавателя</button>
    </router-link>
  </div>
  <FooterComp class="footer"></FooterComp>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 85vh;
  padding-top: 50px;
}

.head {
  font-family: "DelaGothicOne", serif;
  margin-bottom: 30px;
  display: inline-block;
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
  word-break: break-word;
}

td {
  border: 1px solid black;
  border-left: none;
  font-family: "Inter", serif;
  color: black;
  padding: 5px;
  word-break: break-word;
}

.define-border {
  border-right: none;
}

.custom {
  border: 2px solid black;
  border-radius: 15px;
  overflow: hidden;
  background-color: white;
}

tr {
  text-align: center;
}

a {
  color: black;
}

.ellipse {
  position: absolute;
  top: 270px;
  width: 85px;
  right: 0;
  z-index: -1;
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

@media (max-width: 1350px) {
  .footer {
    display: none;
  }
}

@media (max-width: 770px) {
  th {
    font-size: 17px;
  }

  td {
    font-size: 12px;
  }

  .ellipse {
    display: none;
  }

  .head {
    margin-left: 2px;
  }

  .button {
    width: 170px;
    font-size: 10px;
  }
}

@media (max-width: 660px) {
  .head {
    margin-top: 40px;
  }
}

@media (max-width: 370px) {
  th {
    font-size: 15px;
  }

  td {
    font-size: 10px;
  }

  .button {
    width: 120px;
  }
}
</style>