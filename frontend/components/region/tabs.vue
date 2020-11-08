<template>

  <v-container>

    <!-- v-tabs goes here -->
    <v-tabs
      v-model="tab"
      background-color="transparent"
      fixed-tabs >

      <!-- for loop for v-tab goes here -->
      <v-tab
        v-for="(item,i) in items" :key=i >

        <v-icon color="blue darken-3" style="padding-right: 8px;">{{ item.icon }}</v-icon>
        {{ item.header }}

      </v-tab>
    </v-tabs>

    <!-- v-tab-items goes here -->
    <v-tabs-items v-model="tab" v-if="selectedRegions && productsChartData">
      <v-tab-item v-for="(value, name, index) in chartData" :key="index"><!--First Tab Content-->
        <v-card
          flat
        >
          <region-tab :chartData=value></region-tab>
        </v-card>
      </v-tab-item> <!--First Tab Content-->

      <!--Product Charts-->
      <v-tab-item>
        <region-products-tab :productsChartData=productsChartData></region-products-tab>
      </v-tab-item>

    </v-tabs-items>

  </v-container>

</template>

<script>

import RegionTab from "@/components/region/components/RegionTab.vue"
import ProductsTab from "@/components/region/components/ProductsTab.vue"

export default {

  name: "tabs",
  props: ["selectedRegions"],
  components: {
    "region-tab": RegionTab,
    "region-products-tab": ProductsTab,
  },

  data() {
    return {

      tab: 0,
      tabItem: 0,
      chartData: null,
      productsChartData: null,

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
      this.getChartData(this.selectedRegions)
      this.getProductsChartData()
    },

    getChartData(selectedRegions) {
      // this function gets chart data and stores in this.chartData
      this.chartData = null
      var url = process.env.BACKEND + "/api/charts/regions/" + selectedRegions.join(',')
      this.$axios.get(url).then((response) => {
        this.chartData = response.data.data
        console.log(response)
      })
    },

    getProductsChartData() {
      // this function gets chart data and stores in this.productsChartData
      this.productsChartData = null
      var url = "https://api.npoint.io/9edddfe434c5405df5dd"

      this.$axios.get(url).then((response) => {
          this.productsChartData = response.data.data
          console.log(response.data.data)
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

</style>
