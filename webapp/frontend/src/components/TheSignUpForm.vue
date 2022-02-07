<template>
<div>

  <base-container>
    <h3>
      Sign Up
    </h3>
    <p v-if="formIsValid == false" class="err">Failed to login! Check your email and password</p>
    <form @submit.prevent="submitForm()" action="">
      <div class="form-item pt-2">
        <label>Enter your email</label>
        <base-input id="email" type="email" v-model="email"></base-input>
      </div>
      <div class="form-item pt-2">
        <label>Enter your username</label>
        <base-input id="username" type="text" v-model="username"></base-input>
      </div>
      <div class="form-item pt-2">
        <label>Enter your password</label>
        <base-input id="password" type="password" v-model="password"></base-input>
      </div>
      <div class="form-item pt-2">
        <label>Confirm your password</label>
        <base-input id="confirmPassword" type="password" v-model="confirmPassword"></base-input>
      </div>
      <base-button class="mt-4">Sign up</base-button>
    </form>
  </base-container>
</div>
</template>

<script>
export default {
  name: "TheSignUpForm",
  data(){
    return {
      email: '',
      password: '',
      confirmPassword: '',
      username: '',
      formIsValid: true,
    }
  },
  methods: {
    async submitForm(){
      this.validateForm();
      if (this.formIsValid) {
        let response = await fetch("http://localhost:8000/api-auth/registration/",{
          method: 'POST',
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            email: this.email,
            username: this.username,
            password: this.password,
          })
        });
        if (response.ok){
          let user = await response.json();
          this.$store.commit('setUserState', {
            isLoggedIn: true,
            username: user.username,
            token_access: user.token_access,
            token_refresh: user.token_refresh,
          })
          localStorage.setItem('neonotes-token', user.token_access)
          localStorage.setItem('neonotes-username', this.username)
          localStorage.setItem('neonotes-token-refresh', user.token_refresh)
          window.location.reload()
        }

      }

    },
    validateForm(){
      this.formIsValid = true;
      if (!this.email.includes('@') && this.email.length < 5){
        this.formIsValid = false;
      }
      if (this.password != this.confirmPassword && this.password.length < 6){
        this.formIsValid = false;
      }
      if (this.username.length < 0){
        this.formIsValid = false;
      }
    }
  }
}
</script>

<style scoped>
.err{
  color: tomato;
}
</style>
