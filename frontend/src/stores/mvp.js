import { defineStore } from 'pinia';
import {watch, reactive} from 'vue';
import router from "@/router/router";

export const useMvpStore =  defineStore("mvp", () => {
    const state = reactive ({
        allLessons: [
          {
              title: "Математический анализ (лек.)",
              groups: [
                  "Б9122-01.03.02сп",
                  "Б9122-01.03.02мкт",
                  "Б9122-01.03.02сцт",
              ],
              id : 0,
              date : null,
              num : '№ 1',
              time : '8:30 - 10:00'
          },
          {
            title: "Математический анализ (прак.)",
            groups: [
              "Б9122-01.03.02сп",
            ],
            id : 1,
            date : null,
              num : '№ 2',
              time : '10:10 - 11:40'
          },
         ],
        passedLessons : []
      })

    const studentsState = reactive({
        students : [
            [{
                id: 0,
                FullName: 'Иван Иванов Иванович',
                group: 'Б9122-01.03.02сп',
                status: false
            },
            {
                id: 1,
                FullName: 'Иван Иванов Иванович',
                group: 'Б9122-01.03.02сп',
                status: false
            },
            {
                id: 2,
                FullName: 'Иван Иванов Иванович',
                group: 'Б9122-01.03.02мкт',
                status: false
            },{
                id: 3,
                FullName: 'Иван Иванов Иванович',
                group: 'Б9122-01.03.02сцт',
                status: false
            },],

            [{
                id: 0,
                FullName: 'Иван Иванов Иванович',
                group: 'Б9122-01.03.02сп',
                status: false
            },
            {
                id: 1,
                FullName: 'Иван Иванов Иванович',
                group: 'Б9122-01.03.02сп',
                status: false
            },]
        ]
    });

    const setStatus = (lesId, studId) => {
        studentsState.students[lesId][studId] = !studentsState.students[lesId][studId];
    };

    const setDate = (lesId, date) => {
        state.allLessons[lesId].date = date;
        state.passedLessons.push(state.allLessons[lesId]);
        router.push('/lessons')
    };

    if (localStorage.getItem("students")){
        studentsState.students = JSON.parse(localStorage.getItem("students")).students;
    }

    if (localStorage.getItem("lessons")){
        state.allLessons = JSON.parse(localStorage.getItem("lessons")).allLessons;
    }

    watch(
        studentsState,
        (studentsVal) => {
            localStorage.setItem("students", JSON.stringify(studentsVal))
        },
        {deep: true }
    );

    watch(
        state,
        (LessonsVal) => {
            localStorage.setItem("lessons", JSON.stringify(LessonsVal))
        },
        {deep: true }
    );

    return {
        state,
        studentsState,
        setStatus,
        setDate,

    }
});