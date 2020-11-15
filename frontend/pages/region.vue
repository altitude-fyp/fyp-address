<template>
  <v-app>
    <!-- region maps go here -->
    <region-map
      @regionSelectedOnMap=updateSelectedRegions
    />

    <v-row style="padding-left: 80px; padding-right: 80px; padding-top: 20px;">
      <!--    Select Regions to Compare Button-->
      <v-col>
        <v-btn
          color="#D9261C"
          class="white--text mb-2 sidebar"
          depressed
          width="240"
          @click=openRegionSelectionDialog>
          Regions to Compare
        </v-btn>

        <region-selection-dialog
          :showRegionSelectionDialog=showRegionSelectionDialog
          @closeRegionSelectionDialogEvent="closeRegionSelectionDialog"
          @submitSelectedRegionsEvent="updateSelectedRegions"
        >
        </region-selection-dialog>
      </v-col>
      <!--    Switch to Country View-->
      <v-col align="right">
        <v-btn
          outlined
          color="#D9261C"
          width="240"
          @click="$router.push({path: '/'})"
        >
          <v-icon left>mdi-eye</v-icon>
          Switch to Country View
        </v-btn>
      </v-col>
    </v-row>


    <!--    Selected Regions List-->
    <h4 style="padding-left: 80px;">
      Selected Regions
    </h4>
    <v-row style="padding-left: 100px; padding-right:80px;">
      <div v-for="item in selectedRegions">
        <v-col>
          <div class="productRegionName">
            {{ item }}
          </div>
        </v-col>
      </div>
    </v-row>


    <v-tabs
      color="#D9261C"
      dense>
      <v-row justify="center">
        <v-tab>
            Region Information
        </v-tab>
        <v-tab>

            Market Segmentation
        </v-tab>
      </v-row>
      <!--Documentation for #REST APIs goes here-->

      <v-tab-item>

        <!--    Select Regions to Compare Modal-->
        <tabs :selected-regions="selectedRegions"/>

      </v-tab-item>
      <!--Documentation for #Explore the APIs goes here-->
      <v-tab-item>

        <MarketSegmentation/>

      </v-tab-item>

    </v-tabs>


  </v-app>
</template>

<script>

import RegionMap from "@/components/region/region-map";
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

<style scoped>
.productRegionName {
  font-size: 20px;
  font-weight: 500;
  text-transform: capitalize;
  color: #215085;
  margin-bottom: 10px;
}

</style>
