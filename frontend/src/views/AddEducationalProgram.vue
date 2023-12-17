<script setup>
import AdminHeaderComp from "@/components/AdminHeaderComp.vue";
import FooterComp from "@/components/FooterComp.vue";
</script>

<template>
  <AdminHeaderComp></AdminHeaderComp>
  <div class="container">
    <h3 class="head">Добавление образовательной программы</h3>
    <img alt="ellipse" class="ellipse" src="../../public/images/ellipse.png">
    <br>
    <label for="name" class="label">Название программы</label>
    <input
        id="name"
        class="form-control input"
        type="text"
    >
    <label for="level" class="label">Уровень образования</label>
    <input
        id="level"
        class="form-control input"
        type="text"
    >
    <label for="person" class="label">Руководитель программы</label>
    <input
        id="person"
        class="form-control input"
        type="text"
    >
    <br>
    <router-link
        to="/lessons"
    >
      <button type="submit" class="button">Добавить программу</button>
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
    font-size: 12px;
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