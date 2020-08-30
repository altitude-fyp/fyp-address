<template>
  <div>
    {{ todo }}

    <div>
      <v-img contain src="https://picsum.photos/300/300"/>
    </div>
  </div>
</template>

<script>
export default {
  // Get data from API
  asyncData({$axios, params: {id}}) {
    return $axios.$get(`https://jsonplaceholder.typicode.com/todos/${id}`)
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
