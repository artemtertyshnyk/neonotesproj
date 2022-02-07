import {createRouter, createWebHistory} from "vue-router";
import MainPage from "@/pages/MainPage";
import NotesList from "@/pages/NotesList";
import NoteDetail from "@/pages/NoteDetail";
import NotFound from "@/pages/NotFound";
import About from "@/pages/About";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: MainPage},
        {path: '/notes', component: NotesList},
        {path: '/notes/:id', props: true, component: NoteDetail},
        {path: '/about', component: About},
        {path: '/:NotFound(.*)', component: NotFound},
    ],
})

export default router;