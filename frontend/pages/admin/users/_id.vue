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
  asyncData({$axios, params: {id}}) {
    return $axios.$get(`https://jsonplaceholder.typicode.com/todos/${id}`)
      .then((todo) => {
        return {
          todo
        }
      })
  },

}
</script>

<style scoped>

</style>
