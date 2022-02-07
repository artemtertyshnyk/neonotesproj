import { createStore } from 'vuex'
import notesModule from './modules/notes.js'

const store = createStore({
    modules: {
        notes: notesModule,
    },
    state(){
        return {
            isLoggedIn: false,
            username: '',
            token_access: '',
            token_refresh: '',
        }
    },
    mutations: {
        setUserState(state, payload){
            state.isLoggedIn = payload.isLoggedIn;
            state.username = payload.username;
            state.token_access = payload.token_access;
            state.token_refresh = payload.token_refresh;
        }
    },
    getters: {
        // eslint-disable-next-line no-unused-vars
        getUserState(state){
            return {
                username: state.username,
                token: state.token_access,
                token_refresh: state.token_refresh,
                isLoggedIn: state.isLoggedIn,
            }
        }
    }
})

export default store
