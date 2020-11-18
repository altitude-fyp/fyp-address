<template>
  <v-app>
    <!-- region maps go here -->
    <region-map
      :marketSegmentation="tabIndex == 1"
      :marketSegmentationRegions=marketSegmentationRegions
      :selectedRegions=selectedRegions
      @regionSelectedOnMap=updateSelectedRegions
    />

    <v-row style="padding-left: 80px; padding-right: 80px; padding-top: 20px;">
      <!-- Select Regions to Compare Button-->
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
      <!-- Switch to Country View-->
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


    <!-- Selected Regions List-->
    <div align="center">
      
        <h4 style="margin-bottom:10px;">
          Selected Regions in Singapore
        </h4>
    
      <span v-for="(item, i) in selectedRegions" :key=i>
          <span class="productRegionName">
            {{ item }}
          </span>
      </span>
    </div>

    <br/><v-divider></v-divider><br/>

    <v-tabs
      v-model=tabIndex
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

        <MarketSegmentation
          @filteredRegionsDataReceived=handleFilteredRegionsDataReceived
          />

      </v-tab-item>

    </v-tabs>


  </v-app>
</template>

<script>

import RegionMap from "@/components/region/region-map";
import tabs from "@/components/region/tabs";
import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel";
import RegionSelectionDialog from "@/components/home/GoogleBottomSheet/components/RegionSelectionDialog";
import MarketSegmentation from "@/components/region/market-segmentation";

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
      tabIndex:0, // 0 if region information, 1 if market segmentation
      selectedRegions: ["bishan"],
      showRegionSelectionDialog: false,

      marketSegmentationRegions: null,
    }
  },

  // asyncData({query: {regions}}) {
  //   return {
  //     coordinates: null,
  //     selectedRegions: regions || [],
  //   }

  // },


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
      console.log("SELECTED REGIONS:", this.selectedRegions, selectedRegions)
      this.selectedRegions = selectedRegions.map(r => r.toLowerCase())
      this.tabIndex = 0
    },

    handleFilteredRegionsDataReceived(data) {
      this.marketSegmentationRegions = data
    }

  },


}
</script>

<style scoped>
.productRegionName {
  font-size: 30px;
  font-weight: 700;
  text-transform: capitalize;
  color: #d29a42;
  margin-bottom: 30px;
  text-align:center;
  margin-left:30px;
  margin-right:30px;
}

</style>
