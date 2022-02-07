<template>
  <input :value="modelValue" :type="type" @input="$emit('update:modelValue', $event.target.value)" :style="{maxWidth: width}" :id="id" :placeholder="placeholder" class="shadow">
</template>

<script>
export default {
  name: "BaseInput",
  props: {
    placeholder: {
      type: String,
      required: false,
      default: '',
    },
    id: {
      type: String,
      required: false,
      default: '',
    },
    width: {
      type: String,
      required: false,
      default: '100%'
    },
    type: {
      type: String,
      required: false,
      default: 'text'
    },
    modelValue: {
      type: String,
      required: false,
      default: ''
    }
  },
}
</script>

<style scoped>
input, textarea {
  display: flex;
  width: 100%;
  border: 0px solid #ccc;
  border-radius: 25px;
  font: inherit;
  outline: 0;
  padding-left: 1rem;
}

input {
  height: 2.5rem;
}

input::placeholder {
  padding-left: 5%;
}
</style>