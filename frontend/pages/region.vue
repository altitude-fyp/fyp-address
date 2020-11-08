<template>
  <v-app>

    <!-- region maps go here -->
    <region-map 
      @regionSelectedOnMap=updateSelectedRegions
      />

    <!-- search bar goes here -->
    <c-s-v-search/>

    SELECTED REGIONS: {{selectedRegions}}

    <!-- region selection dialog goes here -->
    <v-row justify="center">

      <v-btn
        color="#004D8E"
        class="white--text mb-2 sidebar"
        depressed
        @click=openRegionSelectionDialog>
        Regions to Compare
      </v-btn>

      <region-selection-dialog
        :showRegionSelectionDialog=showRegionSelectionDialog
        @closeRegionSelectionDialogEvent="closeRegionSelectionDialog"
        @submitSelectedRegionsEvent="updateSelectedRegions" />

    </v-row>

    <!-- tabs go here -->
    <tabs :selected-regions="selectedRegions"/>

  </v-app>
</template>

<script>

import RegionMap from "@/components/region/region-map";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";
import RegionSelectionDialog from "@/components/home/GoogleBottomSheet/components/RegionSelectionDialog";

export default {

  name: "region",
  
  components: {
    RegionSelectionDialog,
    MetadataPanel,
    tabs,
    CSVSearch, 
    "region-map": RegionMap
  },

  data() {

    return {
      showRegionSelectionDialog: false,
    }
  },

  asyncData({query: {regions}}) {
    return {
      coordinates: null,
      selectedRegions: regions || [],
    }

  },


  methods: {
    showMarkers(coordinates) {
      this.coordinates = coordinates
    },
    /*getEverything() {
      //this function renders everything based on this.selectedRegions
      this.$axios.get(process.env.BACKEND + "/api/charts/regions/" + this.selectedRegions.join(','))
        .then((response) => {
          this.re = response.data
          console.log(response)
          // sends countriesMetadata, which contains lat lon data, to parent component
        })*/
    openRegionSelectionDialog() {
      // this function is called when the user clicks on "region to compare"
      //this function opens the country selection dialog
      this.showRegionSelectionDialog = true
    },

    closeRegionSelectionDialog() {
      //this function closes the region selection dialog
      this.showRegionSelectionDialog = false
    },

    updateSelectedRegions(selectedRegions) {
      //this function is called after user submits his selected countries from the country selection dialog
      console.log(selectedRegions)
      this.selectedRegions = selectedRegions
    },

  },


}
</script>
