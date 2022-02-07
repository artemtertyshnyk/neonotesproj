<template>
  <div class="base-container shadow" :style="{'flex-direction': direction}">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "BaseContainer",
  props: {
    direction: {
      type: String,
      required: false,
      default: 'row'
    }
  }
}
</script>

<style scoped>
.base-container{
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding:0.5rem;
  margin: 1.5rem auto;
  max-width: 100rem;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
