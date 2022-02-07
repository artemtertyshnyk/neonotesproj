<template>
  <div ref="container">
    <label @click.self="activate" :for="name"><slot></slot></label>
    <input :id="name" :value="name" type="checkbox">
  </div>
</template>
<script>
export default {
  name: "BaseBadge",
  props:['name', 'model'],
  methods: {
    activate(){
      this.$refs.container.classList.toggle('active');
    }
  },
}
</script>

<style scoped>
div{
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
  padding: 0.75rem 1.5rem;
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