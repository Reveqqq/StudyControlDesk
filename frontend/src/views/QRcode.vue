<script setup>
import HeaderComp from "@/components/HeaderComp.vue";
</script>

<template>
  <HeaderComp></HeaderComp>
  <div class="container">
    <img alt="qrcode" class="qrcode" src="../../public/images/qr-code.png">
    <br>
    <router-link
        to="/attendance"
        class="button"
    >
    <button class="button">Назад</button>
    </router-link>
  </div>
</template>

<style scoped>
.container {
  width: 100vw;
  height: 87vh;
  padding-top: 50px;
}

.qrcode {
  width: 40%;
  display: block;
  margin: 0 auto;
}

.button {
  width: 150px;
  height: 35px;
  background-color: #ABDCFF;
  border: none;
  font-family: DelaGothicOne, serif;
  font-size: 15px;
  color: #2B75B9;
  display: block;
  margin: 0 auto;
  text-decoration: none;
}

@media (max-width: 500px) {
  .button {
    width: 100px;
    font-size: 0.9em;
  }
}
</style>