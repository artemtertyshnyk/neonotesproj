<template>
  <div class="root">
    <base-container>
      <h1>Neonotes helper</h1>
    </base-container>
    <base-container class="notes">
      <ul>
        <li v-for="note in notes" :key="note">
          <label :for="note" :class="{active: note === activeNotes[0]}"> <h3>{{ note }}</h3> </label>
          <input :id="note" style="width: 0; height:0;" type="checkbox" v-model="activeNotes" :value="note">
        </li>
      </ul>
    </base-container>
    <base-container direction="column">
      <h3>Currently selected text: </h3>
      <p> {{ selection }} </p>
      <img :src="imageSrc">
    </base-container>
    <button @click="sendChanges"> Send </button>
  </div>
</template>

<script>
import BaseContainer from "../layout/BaseContainer";
import BaseButton from "../layout/BaseButton";

export default {
  name: "DefaultPage",
  components: {BaseContainer, BaseButton},
  data(){
    return {
      selection: '',
      imageSrc: '',
      notes: [],
      notesItems: [],
      activeNotes: [],
      currentId: '',
      text: null,
      token: '',
    }
  },
  async created() {
    let self = this;
    chrome.runtime.sendMessage({message: "get selection"}, res => {
      self.selection = res.selection.text;
      self.imageSrc = res.selection.image;
    });
    let token = ''
    chrome.storage.sync.get('neonotes-token', async res => {
      token = res['neonotes-token'];
      self.token = token;
      if (token){
        let response = await fetch('http://localhost:8000/api/v1/notes/', {
          method: "GET",
          headers: {
            "Authorization": `Bearer ${token}`
          }
        });
        if (response.ok){
          let data = await response.json();
          data.forEach(item => {
            self.notes.push(item.title);
            self.notesItems.push(item);
          })
        } else {
          console.log('oops')
        }
      } else {
        console.log('no token')
      }
    })

  },
  methods: {
    async sendChanges() {
      console.log('started sending!')
      const activeNote = this.activeNotes[0];
      const currentItem = this.notesItems.find( item => item.title === activeNote);
      const currentId = currentItem.id;
      const currentTheme = currentItem.theme;
      let text = JSON.parse(currentItem.text);
      console.log('text')
      console.log(text)
      let toAdd = [];
      if (this.imageSrc){
        toAdd = [{insert: this.selection}]
      } else {
        toAdd = [{insert: this.selection}, {insert: {image: this.imageSrc}}]
      }
      console.log('awdaw')
      console.log(text.ops)
      // let finished = JSON.stringify([text, ...toAdd])
      text.ops.push(...toAdd)
      let finished = JSON.stringify(text)
      console.log(finished)
      let response = await fetch(`http://localhost:8000/api/v1/notes/${currentId}/`, {
        method: 'PUT',
        headers: {
          "Authorization": `Bearer ${this.token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          title: activeNote,
          theme: currentTheme,
          text: finished
        })
      });
      if (response.ok){
        console.log('successfully saved')
      } else {
        console.log('failed to save')
      }
    },
  },
  watch: {
    activeNotes(){
      if (this.activeNotes.length > 1){
        this.activeNotes.shift()
      }


    }
  }
}
</script>

<style scoped>
.root{
  min-width: 300px;
  display: flex;
  justify-content: center;
  flex-direction: column;
}
ul{
  list-style: none;
  margin: 0;
  padding: 0;
  height: 100px;
}
img{
  max-width: 200px;
  height: auto;
}
.notes{
  overflow-y: scroll;
  width: 250px;
  display: flex;
  height: 100px;
}
li {
}
.active{
  color: #3a0061;
}
</style>
