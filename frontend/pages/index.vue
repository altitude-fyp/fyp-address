<template>

  <!--This is the main page where it is just '/'-->
  <v-app>
<<<<<<< HEAD

    <google-map :coordinates="coordinates"/>
    <!-- <c-s-v-search/> -->

    <google-bottom-sheet
      @changeInSelectedCountries="updateMainCoordinates">
    </google-bottom-sheet>

=======
    <google-map :coordinates="coordinates"/>
    <c-s-v-search/>
    <google-bottom-sheet/>
>>>>>>> 3f093c051a0b5c71de9620d0eded2f8afc53e3c5
  </v-app>

</template>

<script>

<<<<<<< HEAD
import GoogleMap from "@/components/home/GoogleMap.vue";
import GoogleBottomSheet from "@/components/home/GoogleBottomSheet/index.vue";
=======

import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";
import CountrySelectionDialog from "@/components/home/GoogleBottomSheet/components/CountrySelectionDialog";
import CountryStatistics from "@/components/home/GoogleBottomSheet/components/CountryStatistics";
import FeatureSelectionPanel from "@/components/home/GoogleBottomSheet/components/FeatureSelectionPanel";
import GoogleBottomSheet from "@/components/home/GoogleBottomSheet";

>>>>>>> 3f093c051a0b5c71de9620d0eded2f8afc53e3c5

export default {

  components: {
<<<<<<< HEAD
    "google-map": GoogleMap,
    "google-bottom-sheet": GoogleBottomSheet 
=======
    GoogleBottomSheet,
    FeatureSelectionPanel,
    CountryStatistics,
    CountrySelectionDialog,
    CSVSearch,
    GoogleMap,

>>>>>>> 3f093c051a0b5c71de9620d0eded2f8afc53e3c5
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
      // insert countriesMetadata from google bottom sheet into this.coordinates
      var out = []
      for (var cname in countriesMetadata) {
        var cdata = countriesMetadata[cname]

        out.push({
          country: cname,
          lat: cdata.lat,
          lon: cdata.lon
        })
      }
      
      this.coordinates = out
    }

  }

}

</script>
