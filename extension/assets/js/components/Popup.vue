<template>
  <component :is="currentComponent"></component>
</template>
<script>
import DefaultPage from "./pages/DefaultPage";
import Auth from "./pages/Auth";
export default {
  components: {DefaultPage, Auth},
  data(){
    return {
      isAuth: true
    }
  },
  computed: {
    currentComponent(){
      if (this.isAuth){
        return 'DefaultPage'
      }
      else{
        return 'Auth'
      }
    }
  },

}


</script>
<style scoped>

</style>
