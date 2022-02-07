<template>
  <router-link @click.stop class="col-lg-3 mx-2 col-12 text-decoration-none text-dark" :to="getLink">
    <base-container >
      <base-container>
        <h3> {{ name }} </h3>
      </base-container>
      <div class="">
        <h5>{{ theme }}</h5>
      </div>
    </base-container>
  </router-link>

</template>

<script>
export default {
  name: "NoteListItem",
  props: ['name', 'theme', 'id'],
  computed: {
    getLink(){
      return this.$route.path + '/' + this.id
    }
  }
}
</script>

<style scoped>
h3{
  color: #3a0061;
}
</style>
