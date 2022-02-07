<template>
  <div class="wrapper">
    <ul>
      <li v-for="theme in currentThemes" :key="theme">
        <div class="badge">
          <label @click="activate" :for="theme">{{ theme }}</label>
          <input v-model="selectedFilters" @change="$emit('activeFilter', selectedFilters)" :id="theme" :value="theme" type="checkbox">
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "TheFilter",
  emits: ['activeFilter'],
  data(){
    return {
      selectedFilters: [],
    }
  },
  methods:{
    activate(event){
      event.target.parentElement.classList.toggle('active');
    }
  },
  computed: {
    currentThemes(){
      return this.$store.getters['notes/getAllThemes']
    }
  }
}
</script>

<style scoped>
ul{
  list-style-type: none;
  margin-left: 0;
  padding-left: 0;
  display: flex;
  flex-direction: row;
}
.wrapper{
  overflow-x: scroll;
  display: flex;
  justify-content: center;
}
.badge{
  transition: all 0.1s ease-in-out;
  font: inherit;
  background-color: transparent;
  color: #3a0061;
  border: 1px solid #3a0061;
  cursor: pointer;
  border-radius: 30px;
  margin-right: 0.5rem;
  display: inline-block;
}
label{
  user-select: none;
  padding: 0.25rem 1.5rem;
}
input{
  width: 0;
}
.active{
  background-color: #3a0061;
  border: 1px solid #3a0061;
  color: white;
}
</style>