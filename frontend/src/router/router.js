import { createRouter, createWebHistory } from "vue-router"
import Login from "@/views/Login.vue";
import MainMenu from "@/views/MainMenu.vue";
import AllLessons from "@/views/AllLessons.vue";
import Lesson from "@/views/Lesson.vue";
import Attendance from "@/views/Attendance.vue";
import PassedLessons from "@/views/PassedLessons.vue";
const routeInfos = [
    {
        path : "/",
        component: Login
    },
    {
        path : "/main_menu",
        component: MainMenu
    },
    {
        path : "/lessons",
        component: AllLessons
    },
    {
        path : "/lesson",
        component: Lesson
    },
    {
        path : "/attendance",
        component: Attendance
    },
    {
        path : "/passed_lessons",
        component: PassedLessons
    }
]

const router = createRouter({
    history : createWebHistory(),
    routes : routeInfos
})

export default router;