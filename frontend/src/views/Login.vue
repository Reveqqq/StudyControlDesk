<script>

export default {
  name: 'Login',
  methods: {
    onMainMenuClick(){
      this.$router.push('/main_menu')
    }
  }
}

</script>

<template>
  <div class="parent" style="width: 100vw; height: 100vh; position: relative">
    <div style="margin: 0 auto">
      <div style="height: 750px; position: relative">
        <img src="../../public/images/fefu5.png" style="width: 300px; top: 3%; left: 3%; position: absolute;">
        <section class="position-absolute top-50 start-50 translate-middle">
          <div style="width: 21rem;">
            <form class="form">
              <h1 class="h1" style="text-align: center; margin-bottom: 20px">Вход</h1>
              <div class="form-outline mb-4">
                <input type="text" name="username" id="id_username" class="form-control" placeholder="Введите логин">
                <div class="form-notch">
                  <div class="form-notch-leading" style="width: 9px;"></div></div></div>
              <div class="form-outline mb-4">
                <input type="password" name="password" id="id_password" class="form-control" placeholder="Введите пароль">
                <div class="form-notch"><div class="form-notch-leading" style="width: 9px;"></div><div class="form-notch-middle" style="width: 64.8px;"></div><div class="form-notch-trailing"></div></div></div>
              <div class="CenteredButton" style="text-align: center">
                <a href="#" @click.prevent="onMainMenuClick()" class="btn btn-primary btn active" role="button" aria-pressed="true">Войти</a>
              </div>
            </form>
          </div>
        </section>
      </div>
      <div class="position-absolute bottom-0 start-50 translate-middle-x" style="height: 25px; border: none; background-color: #a1d14a; width: 2000px; z-index: 0"></div>
      <img src="../../public/images/fefu8.png" class="position-absolute bottom-0 start-50 translate-middle-x" style="width: 550px; z-index: 1">
    </div>
  </div>
</template>

<style scoped>
body {
  margin: 0;
  overflow: hidden;
}

.h1 {
  font-family: 'Ubuntu', sans-serif;
  color: black;
  font-weight: lighter;
  font-style: italic;
}

.line {
  height: 25px;
  border: none;
  background-color: #a1d14a;
  width: 2000px;
  z-index: 1;
}

.parent {
  background-color: lightblue;
  z-index: 0;
}
</style>