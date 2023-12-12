<script>
import FooterComp from "@/components/FooterComp.vue";
import Login from "@/views/Login.vue";

export default {
  name: 'Registration',
  components: { FooterComp, Login },
  methods: {
    onLoginClick() {
      this.$router.push('/')
    }
  }
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
        <input id="name" class="form-control input" type="text">
        <label for="surname" class="label">Введите свою фамилию:</label>
        <input id="surname" class="form-control input" type="text">
        <label for="patronymic" class="label">Введите своё отчество:</label>
        <input id="patronymic" class="form-control input" type="text">
        <label for="email" class="label">Введите свою электронную почту:</label>
        <input id="email" class="form-control input" type="email">
        <button class="button" type="submit">Зарегистрироваться</button><br>
        <a class="account" @click.prevent=onLoginClick() href="#">У меня уже есть аккаунт</a>
      </div>
    </div>
  </div>
  <FooterComp></FooterComp>
</template>

<style scoped>
body {
  margin: 0;
}

.line {
  position: absolute;
  z-index: -1;
}

.formula1 {
  position: absolute;
  top: 350px;
  left: 150px;
  z-index: -1;
}

.formula2 {
  position: absolute;
  left: 1000px;
  top: 120px;
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
</style>