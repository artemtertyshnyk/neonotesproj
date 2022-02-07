<template>
<section class="summarization">
  <div class="slider-container mb-2">
    <label for="range-slider" class="mb-2"> Summarize to: {{percentage}}% </label>
    <input id="range-slider" class="mb-3" type="range" min="1" max="100" v-model="percentage">
  </div>
  <base-button @click="setPercentage">Summarize</base-button>
</section>
  <section>
    <div class="search-container mt-2">
      <base-button @click="findInfo">Search for information</base-button>
    </div>
  </section>
</template>

<script>
export default {
  name: "TheOptionsBar",
  emits: ['setPercentage', 'search'],
  data(){
    return {
      percentage: 50
    }
  },
  computed: {
  },
  methods: {
    setPercentage(){
      this.$emit('percentage', this.percentage)
    },
    async findInfo(){
      this.$emit('search')
    }
  }
}
</script>

<style scoped>
.slider-container{
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
#range-slider{
  width: 20%;
}

</style>
