<template>
  <!--This is the main page where it is just '/'-->
  <v-app>
    <google-map :coordinates="coordinates"/>
    <!-- <c-s-v-search/> -->
    <GoogleBottomSheet @load-coordinates="showMarkers"/>
  </v-app>
</template>

<script>

import GoogleMap from "@/components/home/GoogleMap";
import GoogleBottomSheet from "~/components/home/GoogleBottomSheet";
import CSVSearch from "@/components/home/CSVSearch";

export default {
  components: {
    CSVSearch,
    GoogleBottomSheet,
    GoogleMap,
  },
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
