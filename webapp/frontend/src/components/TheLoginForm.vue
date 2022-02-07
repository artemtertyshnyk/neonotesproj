<template>
  <div>
    <base-container>
      <h3>Log in</h3>
      <form @submit.prevent="submitForm()" action="">
        <div class="form-item pt-2">
          <label>Enter your username</label>
          <base-input id="username" type="text" v-model="username"></base-input>
        </div>
        <div class="form-item text-right pt-2">
          <label>Enter your password </label>
          <base-input id="password" type="password" v-model="password"></base-input>
        </div>
        <base-button class="mt-4">Log In</base-button>
      </form>
    </base-container>

  </div>
</template>

<script>
export default {
  name: "TheLoginForm",
  data() {
    return {
      email: '',
      password: '',
      username: '',
      formIsValid: true,
    }
  },
  methods: {
    validateForm() {
      if (!this.email.includes('@') || this.password.length < 6) {
        this.formIsValid = false;
      }
    },
    async submitForm(){
      if (this.formIsValid) {
        let response = await fetch("http://localhost:8000/api/v1/token/",{
          method: 'POST',
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            username: this.username,
            password: this.password,
          })
        });
        if (response.ok){
          let user = await response.json();
          this.$store.commit('setUserState', {
            isLoggedIn: true,
            username: this.username,
            token_access: user.access,
            token_refresh: user.refresh,
          })
          localStorage.setItem('neonotes-token', user.access)
          localStorage.setItem('neonotes-username', this.username)
          localStorage.setItem('neonotes-token-refresh', user.refresh)
          window.location.reload()
        }


      }
    }
  }
}
</script>

<style scoped>

</style>
