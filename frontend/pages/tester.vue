<template>
  <v-container>
    <v-row>
      <div>
        {{ todo }}
      </div>
    </v-row>

  </v-container>

</template>

<script>
export default {
  name: "tester",
  asyncData({$axios}) {
    return $axios.$post('http://lzl.blue/api/countries/', {
      "countries": [
        "Singapore"
      ]
    }).then((todo) => {
      return {
        todo // Put inside an object
      }
    })
  },
}


</script>

<style scoped>

</style>
