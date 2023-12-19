<script setup>
import AdminHeaderComp from "@/components/AdminHeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
import {reactive} from "vue";
import {useMvpStore} from "@/stores/mvp";

const mvpStore = useMvpStore();

const state = reactive({
  newTeacher:{
    fullname: '',
    school: '',
    mail : '',
  },
})

</script>

<template>
  <AdminHeaderComp></AdminHeaderComp>
  <div class="container">
    <h3 class="head">Добавление преподавателя</h3>
    <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
    <br>
    <label for="name" class="label">ФИО</label>
    <input
        id="name"
        class="form-control input"
        type="text"
        v-model="state.newTeacher.fullname"
    >
    <label for="department" class="label">Школа/институт</label>
    <input
        id="department"
        class="form-control input"
        type="text"
        v-model="state.newTeacher.school"
    >
    <label for="mail" class="label">E-mail</label>
    <input
        id="mail"
        class="form-control input"
        type="email"
        v-model="state.newTeacher.mail"
    >
    <br>
    <router-link
        to="/admin/teachers"
    >
      <button @click="mvpStore.addTeacher(state.newTeacher)" type="submit" class="button">Добавить преподавателя</button>
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

.ellipse {
  position: absolute;
  top: 270px;
  width: 85px;
  right: 0;
  z-index: -1;
}

.head {
  font-family: "DelaGothicOne", serif;
  margin-bottom: 30px;
  display: inline-block;
}

.input {
  width: 300px;
  background-color: #e7e7e7;
  border: 1px lightgray solid;
  margin-left: 5px;
  box-shadow: 0 2px 3px #a8a8a8;
  margin-bottom: 25px;
}

.label {
  font-family: MyriadaPro, serif;
  margin-left: 5px;
  font-size: 25px;
  margin-bottom: 10px;
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

@media (max-width: 660px) {
  .head {
    margin-top: 50px;
  }

  .button {
    width: 170px;
    font-size: 10px;
  }

  .input {
    width: 230px;
  }

  .label {
    font-size: 20px;
  }

  .ellipse {
    display: none;
  }
}
</style>