<template>
  <the-header></the-header>
  <router-view></router-view>
</template>

<script>
import TheHeader from "@/components/TheHeader";
export default {
  name: 'App',
  components: {TheHeader},
  data(){
    return {
      isLoggedIn: false,
      username: '',
      token: '',
    }
  },
  async created() {
    const token = localStorage.getItem('neonotes-token')
    if (token) {
      this.isLoggedIn = true;
      this.$store.commit('setUserState',
          {
            username: localStorage.getItem('neonotes-username'),
            token_access: token,
            token_refresh: localStorage.getItem('neonotes-token-refresh'),
            isLoggedIn: this.isLoggedIn
          }
      )
    }
    else{
      this.isLoggedIn = false
    }
  }
}
</script>

<style>
#app {
  padding: 0;
  margin: 0;
  text-align: center;
}
</style>
