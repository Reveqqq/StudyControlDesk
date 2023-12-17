import { createRouter, createWebHistory } from "vue-router"
import Login from "@/views/LoginPage.vue";
import AllLessons from "@/views/AllLessons.vue";
import Lesson from "@/views/LessonPage.vue";
import Attendance from "@/views/AttendancePage.vue";
import PassedLessons from "@/views/PassedLessons.vue";
import Registration from "@/views/RegistrationPage.vue";
import QRcode from "@/views/QRcode.vue";
import Groups from "@/views/Groups.vue";
import EducationalPrograms from "@/views/EducationalPrograms.vue";
import Teachers from "@/views/Teachers.vue";
import AddGroup from "@/views/AddGroup.vue";
import AddEducationalProgram from "@/views/AddEducationalProgram.vue";
import AddTeacher from "@/views/AddTeacher.vue";
import AdminLogin from "@/views/AdminLogin.vue";
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
    },
    {
        path: '/admin',
        component: AdminLogin
    },
    {
        path: '/admin/groups',
        component: Groups
    },
    {
        path: '/admin/programs',
        component: EducationalPrograms
    },
    {
        path: '/admin/teachers',
        component: Teachers
    },
    {
        path: '/admin/add_group',
        component: AddGroup
    },
    {
        path: '/admin/add_program',
        component: AddEducationalProgram
    },
    {
        path: '/admin/add_teacher',
        component: AddTeacher
    }
]

const router = createRouter({
    history : createWebHistory(),
    routes : routeInfos
})

export default router;