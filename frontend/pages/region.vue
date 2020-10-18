<template>
  <v-app>
    <google-map :coordinates="coordinates"/>
    <c-s-v-search/>
    <MetadataPanel/>
    <tabs/>
  </v-app>
</template>

<script>
import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";

export default {
  name: "region",
  components: {MetadataPanel, tabs, CSVSearch, GoogleMap},

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
