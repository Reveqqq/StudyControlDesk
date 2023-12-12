<script setup>
import {ref} from 'vue';
import FooterComp from "../components/FooterComp.vue";
const username = ref('');
const password = ref('');

function onSubmit () {
      //TODO: Запрос на API на авторизацию  
  window.location.href = '/lessons';
}

</script>

<template>
  <div class="container">
    <img alt="department" class="image" src="../../public/images/logo_department.png">
    <div class="wrapper">
      <div class="login">
        <h5 class="head">Вход</h5>
        <label for="username" class="label">Введите логин:</label>
        <input
        id="username" 
        class="form-control input" 
        type="text"
        v-model="username"
        >
        <label for="password" class="label">Введите пароль:</label>
        <input 
        id="password" 
        class="form-control input" 
        type="password"
        v-model="password"
        >
        <button class="button" type="submit" @click.prevent=onSubmit()>Войти</button><br>
        <router-link
        to="/registration"
        class="account"
        >
          <a class="account">У меня ещё нет аккаунта</a>
        </router-link>
        </div>
    </div>
  </div>
  <FooterComp></FooterComp>
</template>

<style scoped>
body {
  margin: 0;
}

.image {
  width: 300px;
  display: block;
  margin: 30px auto 0;
}

.container {
  width: 100vw;
  height: 100vh;
}

.wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 85vh;
  margin-top: 10px;
}

.head {
  text-align: center;
  font-family: "DelaGothicOne", serif;
  margin-top: 20px;
}

.label {
  margin-left: 25px;
  margin-top: 10px;
  font-family: "Inter", serif;
  font-size: 13px;
  font-weight: bold;
}

.login {
  width: 330px;
  height: 370px;
  border: 2px solid black;
  border-radius: 15px;
}

.input {
  width: 280px;
  background-color: #e7e7e7;
  border: 1px lightgray solid;
  margin: 5px auto 0;
  box-shadow: 0 2px 3px #a8a8a8;
}

.button {
  width: 280px;
  height: 45px;
  margin-left: 23px;
  border: none;
  background-color: black;
  border-radius: 5px;
  color: white;
  font-family: "DelaGothicOne", serif;
  margin-top: 50px;
  box-shadow: 0 2px 3px #a8a8a8;
}

.account {
  font-size: 12px;
  color: black;
  display: block;
  text-align: center;
  margin-top: 30px;
  font-family: Inter, serif;
  font-weight: bolder;
}

@font-face {
  font-family: "MyriadaPro";
  src: url("../../public/fonts/MYRIADPRO-COND.OTF");
}

@font-face {
  font-family: "DelaGothicOne";
  src: url("../../public/fonts/DelaGothicOne-Regular.ttf");
}

@font-face {
  font-family: "PlayfairDisplay";
  src: url("../../public/fonts/PlayfairDisplay.ttf");
}

@font-face {
  font-family: "Montserrat";
  src: url("../../public/fonts/Montserrat-Medium.ttf");
}

@font-face {
  font-family: "Inter";
  src: url("../../public/fonts/Inter-Light.ttf");
}
</style>