<template>

  <!--This is the main page where it is just '/'-->
  <v-app>
     <google-map :coordinates="coordinates"/>
     <c-s-v-search/>
    <v-container>
      <country-selection-dialog/>
      <country-statistics/>
      <feature-selection-panel/>
    </v-container>

  </v-app>

</template>

<script>



import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";
import CountrySelectionDialog from "@/components/home/GoogleBottomSheet/components/CountrySelectionDialog";
import CountryStatistics from "@/components/home/GoogleBottomSheet/components/CountryStatistics";
import FeatureSelectionPanel from "@/components/home/GoogleBottomSheet/components/FeatureSelectionPanel";


export default {
  components: {
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
  },
}
</script>
