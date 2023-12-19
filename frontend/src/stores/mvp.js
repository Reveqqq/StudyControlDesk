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

    const adminState = reactive({
        groups: [{
            title: 'Б9122-01.03.02сп',
            educationalLevel: 'Бакалавриат',
            educationalProgram : 'Прикладная математика и информатика',
        },
        ],
        teachers: [{
            fullname: 'Зиновьев Павел Владимирович',
            school: 'Институт Математики и Компьютерных Технологий',
            mail: 'zinovev.pv@dvfu.ru',
        },
        ],
        educationalPrograms: [{
            title: 'Прикладная математика и информатика',
            educationalLevel: 'Бакалавриат',
            director: 'Сущенко Андрей Андреевич',
        },
        ],
    })

    const addGroup = (newGroup) => {
        adminState.groups.push(newGroup);
    }

    const addTeacher = (newTeacher) => {
        adminState.teachers.push(newTeacher);
    }

    const addEdProg = (newEdProg) => {
        adminState.educationalPrograms.push(newEdProg);
    }

    const setStatus = (lesId, studId) => {
        studentsState.students[lesId][studId] = !studentsState.students[lesId][studId];
    };

    const setDate = (lesId, date) => {
        if (state.allLessons[lesId].date === null) {
            state.allLessons[lesId].date = date;
            state.passedLessons.push(state.allLessons[lesId]);
        }
        router.push('/lessons')
    };

    if (localStorage.getItem("students")){
        studentsState.students = JSON.parse(localStorage.getItem("students")).students;
    }

    if (localStorage.getItem("lessons")){
        state.allLessons = JSON.parse(localStorage.getItem("lessons")).allLessons;
        state.passedLessons = JSON.parse(localStorage.getItem("lessons")).passedLessons;
    }

    if (localStorage.getItem("admin")){
        adminState.groups = JSON.parse(localStorage.getItem("admin")).groups;
        adminState.teachers = JSON.parse(localStorage.getItem("admin")).teachers;
        adminState.educationalPrograms = JSON.parse(localStorage.getItem("admin")).educationalPrograms;
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

    watch(
        adminState,
        (adminVal) => {
            localStorage.setItem("admin", JSON.stringify(adminVal))
        },
        {deep: true }
    );

    return {
        state,
        studentsState,
        adminState,
        setStatus,
        setDate,
        addGroup,
        addTeacher,
        addEdProg,
    }
});