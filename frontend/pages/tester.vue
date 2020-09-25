<template>
  <v-container>
    <v-row>
      {{todo.status}}
    </v-row>
    {{todo}}
  </v-container>

</template>

<script>
export default {
  name: "tester",
  asyncData({$axios}) {
    return $axios.$get(`http://lzl.blue/api/filter/Singapore/`)
      .then((todo) => {
        return {
          todo // Put inside an object
        }
      })
  },
}

</script>

<style scoped>

</style>
