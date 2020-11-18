<template>

  <v-container>

    <!-- v-tabs goes here -->
    <v-tabs
      v-model="tab"
      background-color="transparent"
      color="#D9261C"
      fixed-tabs
      hide-slider>

      <!-- for loop for v-tab goes here -->
      <v-tab
        v-for="(item,i) in items" :key=i >

        <v-icon color="#D9261C" style="padding-right: 8px;">{{ item.icon }}</v-icon>
        {{ item.header }}

      </v-tab>
    </v-tabs>

    <!-- v-tab-items goes here -->
    <v-tabs-items v-model="tab" v-if="selectedRegions && onemapSummaryData && productsChartData && chartData">
      <v-tab-item v-for="(value, name, index) in chartData" :key="index"><!--First Tab Content-->
        <v-card
          flat
        >

        <br/>

        <!-- OneMap Summary Data -->
        <div v-if="index === 0 && onemapSummaryData && selectedRegions">
          <onemap-summary :onemapSummaryData=onemapSummaryData :selectedRegions="selectedRegions"></onemap-summary>
        </div>

          <region-tab :chartData=value></region-tab>
        </v-card>
      </v-tab-item> <!--First Tab Content-->

      <!--Product Charts-->
      <v-tab-item v-if="chartData ">
        <region-products-tab :productsChartData=productsChartData></region-products-tab>
      </v-tab-item>

    </v-tabs-items>

  </v-container>

</template>

<script>

import RegionTab from "@/components/region/components/RegionTab.vue"
import ProductsTab from "@/components/region/components/ProductsTab.vue"
import OneMapSummary from "@/components/region/components/OneMapSummary.vue"

export default {

  name: "tabs",
  props: ["selectedRegions"],
  components: {
    "region-tab": RegionTab,
    "region-products-tab": ProductsTab,
    "onemap-summary": OneMapSummary,
  },

  data() {
    return {

      tab: 0,
      tabItem: 0,
      chartData: null,
      productsChartData: null,
      onemapSummaryData:null,

      items: [
        {
          header: 'At a glance',
          icon: 'mdi-magnify-scan'
        },
        {
          header: 'Economy',
          icon: 'mdi-earth'
        },
        {
          header: 'Society',
          icon: 'mdi-handshake'
        },
        {
          header: 'Household',
          icon: 'mdi-home'
        },
        {
          header: 'Citi Products',
          icon: 'mdi-cash-multiple'
        }
      ]
    }
  },

  mounted() {
    this.getEverything()
  },

  methods: {
    getEverything() {
      this.getOneMapSummaryData()
      this.getChartData(this.selectedRegions)
      this.getProductsChartData(this.selectedRegions)
    },

    getChartData(selectedRegions) {
      // this function gets chart data and stores in this.chartData
      this.chartData = null
      var url = process.env.BACKEND + "/api/charts/regions/" + selectedRegions.join(',')
      this.$axios.get(url).then((response) => {
        this.chartData = response.data.data
        this.isLoaded = true
      })
    },

    getProductsChartData(selectedRegions) {
      // this function gets chart data and stores in this.productsChartData
      this.productsChartData = null
      var selectedRegions = selectedRegions.map(region => region.toLowerCase());
      var url = process.env.BACKEND + "/api/finance/" + selectedRegions.join(',')
      this.$axios.get(url).then((response) => {
          this.productsChartData = response.data.data
      })
    },

    getOneMapSummaryData() {
      // this function gets the OneMap summary data for the region
      this.onemapSummaryData = null
      var url = process.env.BACKEND + "/api/regions/summary"

      this.$axios.get(url).then((response) => {
          this.onemapSummaryData = response.data
          this.isLoaded = true
      })
    },
  },

  watch: {
    selectedRegions: function (n,o) {
      this.getEverything()
    }
  }
}
</script>

<style scoped>
.productRegionName {
  font-size:20px;
  font-weight:700;
  text-transform:capitalize;
  color:#215085;
  margin-bottom:10px;
}

</style>