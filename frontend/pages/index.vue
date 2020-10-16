<template>
  
  <!--This is the main page where it is just '/'-->
  <v-app>

    <google-map :coordinates="coordinates"/>
    <!-- <c-s-v-search/> -->

    <google-bottom-sheet
      @changeInSelectedCountries="updateMainCoordinates">
    </google-bottom-sheet>

  </v-app>

</template>

<script>

import GoogleMap from "@/components/home/GoogleMap.vue";
import GoogleBottomSheet from "@/components/home/GoogleBottomSheet/index.vue";

export default {

  components: {
    "google-map": GoogleMap,
    "google-bottom-sheet": GoogleBottomSheet 
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

    updateMainCoordinates(countriesMetadata) {
      this.coordinates = [{lat: 1.3521, lng: 103.8198}]
    }

  }

}

</script>
