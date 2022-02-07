<template>
  <div class="base-container shadow">
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: "BaseContainer"
}
</script>

<style scoped>
.base-container{
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
  margin: 2rem auto;
  max-width: 100rem;
}
</style>