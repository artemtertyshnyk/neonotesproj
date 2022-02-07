<template>
  <base-container>
    <h2> {{ name }} </h2>
    <base-button @click="deleteNote">Delete</base-button>
    <the-options-bar @percentage="summarization" @search="searchInfo"></the-options-bar>
    <base-container v-if="showPreview" class="sum-preview">
      <h3>Preview</h3>
      <p>{{ preparedSummText }}</p>
      <base-button @click="applySumm">Apply</base-button>
      <base-button @click="cancelSumm">Cancel</base-button>
    </base-container>
    <base-container class="editor-container">
      <div class="editor" ref="editor"></div>
    </base-container>
    <base-button @click="saveAndSendData">Save changes</base-button>
  </base-container>
</template>

<script>
import Quill from 'quill'
import TheOptionsBar from "../components/TheOptionsBar";

const defaultOptions = {
  theme: 'snow',
  boundary: document.body,
  modules: {
    toolbar: [
      ['bold', 'italic', 'underline', 'strike'],
      ['blockquote', 'code-block'],
      [{ 'header': 1 }, { 'header': 2 }],
      [{ 'list': 'ordered' }, { 'list': 'bullet' }],
      [{ 'script': 'sub' }, { 'script': 'super' }],
      [{ 'size': ['small', false, 'large', 'huge'] }],
      [{ 'color': ['tomato', 'black', 'green', 'blue'] }, { 'background': ['tomato', 'black', 'white', 'lightblue'] }],
      [{ 'font': [] }],
      [{ 'align': [] }],
      ['clean'],
      ['link', 'image', 'video'],
    ],
  },
  placeholder: 'Insert text here ...',
  readOnly: false
}

export default {
  name: "NoteDetail",
  components: {TheOptionsBar},
  props: ['id'],
  data(){
    return {
      text: null,
      name: '',
      noteId: null,
      theme: '',
      percentage: 100,
      showPreview: false,
      summPreview: ''
    }
  },
  async created(){
      const token = this.$store.getters['notes/getUserState'].token;
      let currentUrl = this.$router.currentRoute.value.path;
      let urlParts = currentUrl.split('/')
      let id = urlParts[urlParts.length - 1]
      this.noteId = id
      let response = await fetch(`http://localhost:8000/api/v1/notes/${id}/`, {
        headers: {
          "Authorization": `Bearer ${token}`
        }
      });
      if (response.ok) {
        let data = await response.json();
        this.text = data.text;
        this.name = data.title;
        this.theme = data.theme;
        this.quill = new Quill(this.$refs.editor, defaultOptions)
        this.quill.setContents(JSON.parse(this.text))
      }
      const humanText = this.quill.getText();
      let nerResp = await fetch(`http://localhost:8000/api/v1/notes/${this.noteId}/`, {
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        method: "PUT",
        body: JSON.stringify({
          text: JSON.stringify(this.quill.getContents()),
          title: this.name,
          theme: this.theme,
          ner: 1,
          text1: humanText
        })
      });
      if (nerResp.ok){
        let data = await nerResp.json();
        let nerText = data.ner_text
        nerText = JSON.parse(nerText.replaceAll("'", '"'))
        Object.keys(nerText).forEach(item => {
          if (item.length > 1){
            this.quill.formatText(this.quill.getText().indexOf(item), item.length,{
              'background': 'lightblue'
            })
          }
        })
      }
      else {
        console.log('failed to get response')
      }


  },
  computed: {
    preparedSummText(){
      return this.summPreview;
    }

  },
  methods: {
    async saveAndSendData(){
      const token = this.$store.getters['notes/getUserState'].token;
      const data = this.quill.getContents();
      let response = await fetch(`http://localhost:8000/api/v1/notes/${this.noteId}/`,{
        method: 'PUT',
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          title: this.name,
          theme: this.theme,
          text: JSON.stringify(data),

        })
      });
      if (response.ok) {
        // eslint-disable-next-line no-unused-vars
        let data = await response.json();
      }else{
        console.log('failed to save')
      }
    },
    async summarization(val){
      const token = this.$store.getters['notes/getUserState'].token;
      this.percentage = val
      const humanText = this.quill.getText();
      const text = this.quill.getContents();
      let response = await fetch(`http://localhost:8000/api/v1/notes/${this.noteId}/`, {
        method: 'PUT',
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          text: JSON.stringify(text),
          text1: humanText,
          theme: this.theme,
          title: this.name,
          summ: 1,
          percent: this.percentage
        })
      });
      if (response.ok){
        let data = await response.json();
        this.summPreview = data.text1;
        this.showPreview = true;
      }
    },
    applySumm(){
      this.quill.setText(this.preparedSummText);
      this.showPreview = false;
    },
    cancelSumm(){
      this.summPreview = null;
      this.showPreview = false;
    },
    async searchInfo(){
      const token = this.$store.getters['notes/getUserState'].token;
      let response = await fetch(`http://localhost:8000/api/v1/notes/${this.noteId}/`, {
        method: 'PUT',
        headers: {
          "Authorization": `Bearer ${token}`,
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          text: JSON.stringify(this.quill.getContents()),
          theme: this.theme,
          text1: this.name,
          title: this.name,
          ner: 0,
          parsing: 1
        })
      });
      if (response.ok){
        let data = await response.json();
        this.quill.insertText(0, data.parsing_text)
      }
    },
    async deleteNote(){
      const token = this.$store.getters['notes/getUserState'].token;
      // eslint-disable-next-line no-unused-vars
      let response = await fetch(`http://localhost:8000/api/v1/notes/${this.noteId}/`, {
        method: 'DELETE',
        headers: {
          "Authorization": `Bearer ${token}`,
        }
      })
    }
  },
}
</script>

<style scoped>
.editor-container{
  max-width: 80rem;
}
.sum-preview{
  max-width: 80rem;
}
</style>
