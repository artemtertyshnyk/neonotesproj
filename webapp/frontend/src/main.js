import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import store from './store/index.js'

import BaseButton from "@/layout/BaseButton";
import BaseContainer from "@/layout/BaseContainer";
import BaseModal from "@/layout/BaseModal";
import BaseInput from "@/layout/BaseInput";
import BaseBadge from "@/layout/BaseBadge";

const app = createApp(App);

app.use(router);
app.use(store);

app.component('base-button', BaseButton);
app.component('base-container', BaseContainer);
app.component('base-modal', BaseModal);
app.component('base-input', BaseInput);
app.component('base-badge', BaseBadge);

app.mount('#app')
