<template>
  <v-app>
    <!--<google-map :coordinates="coordinates"/>-->
    <!--    Here is just a padding because Region to Compare button is getting blocked-->
    <div style="margin-top:50px"></div>

    [[ POLYGON MAP WILL COME HERE ]]

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
import GoogleMap from "@/components/home/GoogleMap";
import CSVSearch from "@/components/home/CSVSearch";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";
import RegionSelectionDialog from "@/components/home/GoogleBottomSheet/components/RegionSelectionDialog";
import MarketSegmentation from "@/components/region/marketSegmentation";

export default {
  name: "region",
  components: {MarketSegmentation, RegionSelectionDialog, MetadataPanel, tabs, CSVSearch, GoogleMap},
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
      this.selectedRegions = selectedRegions
      console.log(selectedRegions)
    },
  },
}
</script>

<style scoped>

</style>
