import { defineStore } from 'pinia';
import {watch, ref} from 'vue';

export const useLessonStore =  defineStore("lesson", () => {
    const lesson = ref({
        id: null,
    });

    const changeId = (newId) => {
        lesson.value.id = newId;
    };

    if (localStorage.getItem("lesson")){
        lesson.value = JSON.parse(localStorage.getItem("lesson"));
    }


    watch(
        lesson,
        (lessonVal) => {
            localStorage.setItem("lesson", JSON.stringify(lessonVal))
        },
        {deep: true }
    );

    return {
        lesson,
        changeId,
    }
});