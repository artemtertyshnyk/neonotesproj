export default {
    namespaced: true,
    state(){
        return {
            notesList: [],
        }
    },
    mutations:{
        fetchLocalNotes(state, payload){
            state.notesList = payload
        },
        saveNote(state, payload){
            const currentNoteIndex = state.notesList.findIndex(el => el.id == payload.id);
            state.notesList[currentNoteIndex].id = payload.id;
            state.notesList[currentNoteIndex].content = payload.content;
        },
    },
    actions: {
        async fetchNotes(state){
            const token = state.getters['getUserState'].token;
            let response = await fetch("http://localhost:8000/api/v1/notes/", {
                method: 'GET',
                headers: {
                    "Authorization": `Bearer ${token}`
                }
            })
            if (response.ok) {
                let notes = await response.json();
                state.commit('fetchLocalNotes', notes)
            }
            else {
                console.log('failed to fetch notes')
                state.commit('fetchLocalNotes', [])
            }
        },
        async addNote(state, payload){
            const token = state.getters['getUserState'].token;
            let response = await fetch('http://localhost:8000/api/v1/notes/', {
                method: 'POST',
                headers: {
                    "Authorization": `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(payload)
            });
            if (response.ok){
                await state.dispatch('fetchNotes');
            }
            else{
                console.log('failed to add')
            }
        }
    },
    getters: {
        // eslint-disable-next-line no-unused-vars
        getUserState(state, getters, rootState, rootGetters){
            return rootGetters['getUserState']
        },
        getNotes(state){
            return state.notesList
        },
        getAllThemes(state){
            const notesList = state.notesList;
            const themeList = [];
            notesList.forEach(item => {
                if (!themeList.includes(item.theme)){
                    themeList.push(item.theme)
                }
            })
            return themeList;
        },
    }
}
