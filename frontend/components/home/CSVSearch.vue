<template>
  <v-toolbar
    dense
    :absolute=true
    floating
    width="1000"
    rounded
  >
    <v-text-field
      hide-details
      prepend-icon="search"
      single-line
    ></v-text-field>

  </v-toolbar>
</template>

<script>
export default {
  name: "CSVSearch"
}
</script>

<style scoped>

</style>
