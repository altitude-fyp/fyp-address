<template>
  
  <!--This is the main page where it is just '/'-->
  <v-app>
    <!-- <google-map :coordinates="coordinates"/> -->
    <!-- <c-s-v-search/> -->
    <!-- <GoogleBottomSheet @load-coordinates="showMarkers"/> -->

    <test></test>

  </v-app>

</template>

<script>



import GoogleMap from "@/components/home/GoogleMap";
import GoogleBottomSheet from "~/components/home/GoogleBottomSheet";
import CSVSearch from "@/components/home/CSVSearch";

import test from "@/components/home/GoogleBottomSheet/index";

export default {
  components: {
    CSVSearch,
    GoogleBottomSheet,
    GoogleMap,
    test
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
