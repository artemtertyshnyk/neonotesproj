<template>
  <template v-if="user.isLoggedIn">
  <base-container>
    <base-button @click="toggleAddForm">Create a note</base-button>
    <transition name="fade">
      <the-add-form @add-note="addNote" v-if="showAddForm"></the-add-form>
    </transition>
  </base-container>
  <base-container>
    <the-filter @activeFilter="getFilters"></the-filter>
  </base-container>
  <base-container>
    <div class="container">
      <div class="row justify-content-center">
        <note-list-item
            v-for="note in notesList"
            :key="note.id"
            :name="note.title"
            :theme="note.theme"
            :id="note.id">
        </note-list-item>
      </div>
    </div>
  </base-container>
  </template>
  <div v-else>
    <h3>Log in at first</h3>
  </div>
</template>

<script>
import BaseContainer from "@/layout/BaseContainer";
import NoteListItem from "@/layout/NoteListItem";
import TheAddForm from "@/components/TheAddForm";
import TheFilter from "@/components/TheFilter";

export default {
  name: "NotesList",
  components: {BaseContainer, NoteListItem, TheAddForm, TheFilter},
  data() {
    return {
      showAddForm: false,
      filterList: [],
      notesList: [],
      user: {},
    }
  },
  async created() {
    this.user = this.$store.getters['getUserState']
    await this.$store.dispatch('notes/fetchNotes')
    this.notesList = this.$store.getters['notes/getNotes'];
  },
  methods: {
    toggleAddForm(){
      this.showAddForm = !this.showAddForm
    },
    async addNote(newName, newTheme) {
      const newNote = {
        title: newName,
        theme: newTheme,
        text: ''
      }
      await this.$store.dispatch('notes/addNote', newNote);
      await this.$store.dispatch('notes/fetchNotes')
      this.notesList = this.$store.getters['notes/getNotes']
    },
    getFilters(filters){
      this.filterList = filters
      let notesList = this.$store.getters['notes/getNotes']
      if (filters.length > 0){
        this.notesList = notesList.filter(item => filters.includes(item.theme) )
      }
      else {
        this.notesList = notesList
      }
    }
  },
}
</script>

<style scoped>
.fade-enter-active, .fade-leave-active {
  transition: opacity .1s ease-out;
}
.fade-enter, .fade-leave-to{
  opacity: 0;
}

</style>
