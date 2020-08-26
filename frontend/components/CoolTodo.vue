<template>
  <div>
    <h1>{{ title }}</h1>
    <h1>{{ id }}</h1>
  </div>
</template>

<script>
export default {
  name: "CoolTodo",
  props: {
    title: {
      type: String
    },
    id: {
      type: String
    },
  }
}
</script>

<style scoped>

</style>
