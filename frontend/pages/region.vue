<template>
  <v-app>
    <!-- <google-map :coordinates="coordinates"/> -->

    <region-map :coordinates="{lat:0, lng:0}" />

    <!-- <c-s-v-search/>
    <MetadataPanel/>
    <tabs/> -->
  </v-app>
</template>

<script>

import RegionMap from "@/components/region/region-map";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";

export default {
  name: "region",
  components: {MetadataPanel, tabs, CSVSearch, 
    "region-map": RegionMap},

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
