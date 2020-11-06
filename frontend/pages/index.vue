<template>

  <!--This is the main page where it is just '/'-->
  <v-app>


    <google-map :coordinates="coordinates"/>
    <c-s-v-search/>
    <google-bottom-sheet
      @changeInSelectedCountries="updateMainCoordinates">
    </google-bottom-sheet>

  </v-app>

</template>

<script>
import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";
import CountrySelectionDialog from "@/components/home/GoogleBottomSheet/components/CountrySelectionDialog";
import CountryStatistics from "@/components/home/GoogleBottomSheet/components/CountryStatistics";
import FeatureSelectionPanel from "@/components/home/GoogleBottomSheet/components/FeatureSelectionPanel";
import GoogleBottomSheet from "@/components/home/GoogleBottomSheet";


export default {

  components: {

    GoogleBottomSheet,
    FeatureSelectionPanel,
    CountryStatistics,
    CountrySelectionDialog,
    CSVSearch,
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
