<script setup>
import {ref} from 'vue';
import FooterComp from "@/components/FooterComp.vue";
const name = ref('');
const surname = ref('');
const patronymic = ref('');
const mail = ref('');
const password = ref('');

function onSubmit () {
  const formData = new URLSearchParams();
  formData.append('email', mail.value);
  formData.append('username', name.value);
  formData.append('password', password.value);
    fetch(process.env.VUE_APP_API_URL + '/users/', {
    method: 'POST',
    body: formData})
  .then(response => response.json())
      .then(data => {
        console.log(data);
        window.location.href = 'lessons';
  }).catch(error => {
    console.error(error);    // Обработка ошибки
  });
}

</script>

<template>
  <img alt="line" class="line" src="../../public/images/background_line1.png">
  <img alt="formula1" class="formula1" src="../../public/images/formula1.png">
  <img alt="formula2" class="formula2" src="../../public/images/formula2.png">
  <div class="container">
    <img alt="department" class="image" src="../../public/images/logo_department.png">
    <div class="wrapper">
      <div class="login">
        <h5 class="head">Регистрация</h5>
        <label for="name" class="label">Введите своё имя:</label>
        <input 
        id="name" 
        class="form-control input" 
        type="text"
        v-model="name"
        >
        <label for="surname" class="label">Введите свою фамилию:</label>
        <input 
        id="surname" 
        class="form-control input" 
        type="text"
        v-model="surname"
        >
        <label for="patronymic" class="label">Введите своё отчество:</label>
        <input 
        id="patronymic" 
        class="form-control input" 
        type="text"
        v-model="patronymic"
        >
        <label for="email" class="label">Введите свою электронную почту:</label>
        <input 
        id="email" 
        class="form-control input" 
        type="email"
        v-model="mail"
        >
        <button class="button" type="submit" @click.prevent=onSubmit()>Зарегистрироваться</button><br>
        <router-link
        to="/"
        class="account"
        >
          <a class="account">У меня уже есть аккаунт</a>
        </router-link>
      </div>
    </div>
  </div>
  <FooterComp class="footer"></FooterComp>
</template>

<style scoped>
body {
  margin: 0;
}

.line {
  position: absolute;
  width: 100%;
  z-index: -1;
  top: 100px;
}

.formula1 {
  position: absolute;
  top: 500px;
  left: 11%;
  z-index: -1;
  width: 22%;
}

.formula2 {
  position: absolute;
  right: 15%;
  top: 150px;
  width: 18%;
  z-index: -1;
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
  font-family: Inter, serif;
  font-size: 13px;
  font-weight: bold;
}

.login {
  width: 330px;
  height: 515px;
  border: 2px solid black;
  border-radius: 15px;
  background-color: white;
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

@media (max-width: 1000px) {
  .formula1 {
    display: none;
  }

  .formula2 {
    display: none;
  }

  .line {
    display: none;
  }

}

@media (max-width: 1350px) {
  .footer {
    display: none;
  }
}

@media (max-width: 360px) {
  .button {
    width: 250px;
  }

  .input {
    width: 250px;
  }

  .image {
    width: 250px;
  }
}
</style>