<template>
  <v-app>
    <google-map :coordinates="coordinates"/>
    <c-s-v-search/>
    <tabs/>
  </v-app>
</template>

<script>
import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";

export default {
  name: "region",
  components: {CountrySelectionDialog, tabs, CSVSearch, GoogleMap},

  data() {
    return {
      coordinates: null
    }
  },
  methods: {
    showMarkers(coordinates) {
      this.coordinates = coordinates
    },
  },
}
</script>

<style scoped>

</style>
