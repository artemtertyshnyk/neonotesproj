<template>
  <section class="mt-1">
    <form @submit.prevent="submitForm" class="d-flex justify-content-center mt-3">
      <base-container>
        <h3>Add a note</h3>
        <div class="form-item">
          <base-input v-model="name" placeholder="Name" id="name"></base-input>
        </div>
        <div class="form-item">
          <base-input v-model="theme" placeholder="Theme" id="theme"></base-input>
        </div>
        <div class="form-item">
          <base-button type="submit">Add</base-button>
        </div>
      </base-container>
    </form>
  </section>
</template>

<script>
export default {
  name: "TheAddForm",
  emits: ['add-note'],
  data(){
    return{
      name: '',
      theme: '',
    }
  },
  methods:{
    submitForm(){
        this.$emit('add-note', this.name, this.theme)
    }
  }
}
</script>

<style scoped>
  h3 {
    color: #3a0061;
  }
.form-item{
  padding-top: 1rem;
}
section {
  transition: all .5s ease-out;
}
</style>
