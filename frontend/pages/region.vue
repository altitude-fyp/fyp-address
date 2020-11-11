<template>
  <v-app>
    <!--    Here is just a padding because Region to Compare button is getting blocked-->
    <div style="margin-top:50px"></div>

    <!-- region maps go here -->
    <region-map
      :selectedRegions=selectedRegions
      @regionSelectedOnMap=updateSelectedRegions
      />

    <!-- search bar goes here -->
    <c-s-v-search/>

    SELECTED REGIONS: {{selectedRegions}}

<!--    Select Regions to Compare Button-->
    <v-row justify="center">

      <v-btn
        color="#004D8E"
        class="white--text mb-2 sidebar"
        depressed
        rounded
        @click=openRegionSelectionDialog>
        Regions to Compare
      </v-btn>

      <region-selection-dialog
        :showRegionSelectionDialog=showRegionSelectionDialog
        @closeRegionSelectionDialogEvent="closeRegionSelectionDialog"
        @submitSelectedRegionsEvent="updateSelectedRegions"
      >
      </region-selection-dialog>

    </v-row>

    <!--    Select Regions to Compare Modal-->
    <tabs :selected-regions="selectedRegions"/>
    <MarketSegmentation/>
  </v-app>
</template>

<script>

import RegionMap from "@/components/region/region-map";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";
import RegionSelectionDialog from "@/components/home/GoogleBottomSheet/components/RegionSelectionDialog";
import MarketSegmentation from "@/components/region/marketSegmentation";

export default {

  name: "region",
  
  components: {
    MarketSegmentation,
    RegionSelectionDialog,
    MetadataPanel,
    tabs,
    CSVSearch, 
    "region-map": RegionMap
  },

  data() {

    return {
      selectedRegions: [],
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
