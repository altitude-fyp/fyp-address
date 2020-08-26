<template>
<!--This is a routing page - Routing /home to / via <script /> -->
</template>

<script>
export default {
  name: "home",
  mounted() {
    this.$router.push({path: "/"})

  }
}
</script>

<style scoped>

</style>
