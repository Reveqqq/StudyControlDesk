<script>
export default {
  name: 'Attendance',
}

</script>

<template>
  <div style="width: 100vw; height: 100vh; position: relative">
  <SideBar></SideBar>
    <div style="height: 100vh; display: inline-block; position: absolute; width: 75vw" class="container">
      <h2 style="text-align: center; font-weight: bold; padding-top: 30px">Математический анализ (прак.) 01.01.2023 16:50-18:20</h2><br>
      <div style="height: 65vh">
        <table class="table table-bordered" id="table" style="text-align: center; position: absolute; margin-left: 30px;">
          <thead class="table table-bordered">
          <tr class="table-primary">
            <th scope="col" class="align-middle">№</th>
            <th scope="col" class="align-middle">Студент</th>
            <th scope="col" class="align-middle">Номер группы</th>
            <th scope="col" class="align-middle">Статус</th>
          </tr>
          <tr>
            <td>1</td>
            <td>ФИО студента</td>
            <td>Б9122-01.03.02сп</td>
            <td>+</td>
          </tr>
          </thead>
        </table>
      </div>
      <div class="CenteredButton" style="text-align: center">
        <a href="#" class="btn btn-primary btn active" role="button" aria-pressed="true">Сохранить</a>
      </div>
    </div>
  </div>
</template>

<style scoped>
h2 {
  font-family: 'Ubantu', sans-serif;
  font-style: italic;
  margin-top: 20px;
}

body {
  width: 100%;
  height: 100vh;
  margin: 0;
  overflow: hidden;
  font-family: 'Ubantu', sans-serif;
}

p {
  font-size: 1.2em;
}

li {
  list-style-type: none;
  padding: 5px;
  margin: 5px;
  width: 200px;
  font-size: 1.2em;
  white-space: nowrap
}
</style>