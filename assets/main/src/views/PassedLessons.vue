<script>
import SideBar from "@/components/SideBar.vue";
export default {
  name: 'PassedLessons',
  components: { SideBar },
  methods: {
    onAttendanceClick() {
      this.$router.push('/attendance')
    }
  }
}
</script>

<template>
  <div style="width: 100vw; height: 100vh; position: relative">
  <SideBar></SideBar>
    <div style="height: 100vh; display: inline-block; position: absolute; width: 75vw" class="container">
      <h2 style="text-align: center; font-weight: bold;">Проведённые занятия</h2><br>
      <div style="height: 80vh">
        <table class="table table-bordered" id="table" style="text-align: center; position: absolute; margin-left: 30px;">
          <thead class="table table-bordered">
          <tr class="table-primary">
            <th scope="col" class="align-middle">№</th>
            <th scope="col" class="align-middle">Предмет</th>
            <th scope="col" class="align-middle">Дата</th>
            <th scope="col" class="align-middle">Номер группы</th>
            <th scope="col" class="align-middle">Редактировать</th>
          </tr>
          <tr>
            <td class="align-middle">1</td>
            <td class="align-middle">Мат. анализ (лек.)</td>
            <td class="align-middle">01.01.2023</td>
            <td class="align-middle">Б9122-01.03.02сп</td>
            <td class="align-middle"><button class="btn btn-class-outline-info shadow-none" type="button" style="border: none;" @click.prevent="onAttendanceClick()">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-square" viewBox="0 0 16 16">
                <path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
                <path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
              </svg>
            </button></td>
          </tr>
          </thead>
        </table>
      </div>
    </div>
  </div>
</template>

<style scoped>
h2 {
  font-family: 'Ubantu', sans-serif;
  font-style: italic;
  margin-top: 45px;
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