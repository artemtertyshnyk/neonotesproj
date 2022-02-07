<template>
  <base-modal @close="hideDialog" :open="dialogIsVisible">
    <component class="pt-2" :is="authMode"></component>
    <base-button @click="setSignUpMode" v-if="authMode === 'TheLoginForm'" :mode="'flat'">Don't have an account? Sign up!</base-button>
    <base-button @click="setLoginMode" v-if="authMode === 'TheSignUpForm'" :mode="'flat'">Already have an account? Log in!</base-button>
  </base-modal>
  <header class="container-fluid shadow mb-4">
      <nav class="navbar navbar-light navbar-expand-lg ">
          <div class="container-fluid p-3 justify-content-around">
            <router-link to="/" class="navbar-brand px-4">
              <img src="../../public/assets/logo.svg" style="width: 150px; height:50px" alt="">
            </router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0" >
              <li class="nav-item px-2">
                <router-link to="/" class="nav-link">Home</router-link>
              </li>
              <li class="nav-item px-2">
                <router-link to="/notes" class="nav-link">Notes List</router-link>
              </li>
<!--              <li class="nav-item px-2">-->
<!--                <router-link to="/about" class="nav-link">About</router-link>-->
<!--              </li>-->
          </ul>
        </div>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                <li v-if="!isLoggedIn" class="nav-item px-2">
                  <base-button @click="showDialog">Log in/Sign up</base-button>
                </li>
                <li v-else class="nav-item px-2">
                  <base-button :mode="'flat'" > {{ username }} </base-button>
                  <base-button :mode="'flat'" @click="logout" > Logout </base-button>
                </li>
              </ul>
            </div>
        </div>
      </nav>
  </header>
</template>

<script>
import TheSignUpForm from "@/components/TheSignUpForm";
import TheLoginForm from "@/components/TheLoginForm";

export default {
  name: "TheHeader",
  components: {
    TheLoginForm,
    TheSignUpForm
  },
  data(){
    return {
      dialogIsVisible: false,
      authMode: 'TheSignUpForm',
      username: '',
      isLoggedIn: false,
    }
  },
  created() {
    const user = this.$store.getters['getUserState'];
    if (user.isLoggedIn){
      this.isLoggedIn = true;
      this.username = user.username;
    }
  },
  methods: {
    hideDialog(){
      this.dialogIsVisible = false
    },
    showDialog(){
      this.dialogIsVisible = true
    },
    setSignUpMode(){
      this.authMode = 'TheSignUpForm'
    },
    setLoginMode(){
      this.authMode = 'TheLoginForm'
    },
    async logout(){
      localStorage.removeItem('neonotes-token');
      localStorage.removeItem('neonotes-username');
      const refresh = localStorage.getItem('neonotes-token-refresh');
      localStorage.removeItem('neonotes-token-refresh');
      let response = await fetch('http://localhost:8000/api/v1/token/refresh/', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          refresh: refresh
        })
      });
      if (response.ok){
        this.$store.commit('setUserState', {
          isLoggedIn: false,
          username: '',
          token_access: '',
          token_refresh: '',
        })
        window.location.reload()
      }
      else{
        console.log('logout error')
      }
    }
  }
}
</script>

<style scoped>
  .navbar-collapse {
    flex-grow: 0;
  }
  .navbar-brand{
    color: #3a0061;
    font-weight: bold;
    font-size: 1.5rem;

  }
</style>
