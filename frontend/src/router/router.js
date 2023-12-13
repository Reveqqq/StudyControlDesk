import { createRouter, createWebHistory } from "vue-router"
import Login from "@/views/LoginPage.vue";
import AllLessons from "@/views/AllLessons.vue";
import Lesson from "@/views/LessonPage.vue";
import Attendance from "@/views/AttendancePage.vue";
import PassedLessons from "@/views/PassedLessons.vue";
import Registration from "@/views/RegistrationPage.vue";
import QRcode from "@/views/QRcode.vue";
const routeInfos = [
    {
        path : "/",
        component: Login
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
    },
    {
        path: "/registration",
        component: Registration
    },
    {
        path: "/qr",
        component: QRcode
    }
]

const router = createRouter({
    history : createWebHistory(),
    routes : routeInfos
})

export default router;