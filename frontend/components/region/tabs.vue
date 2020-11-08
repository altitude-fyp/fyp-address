<template>
  <v-container>
    <v-tabs
      v-model="tab"
      background-color="transparent"
      fixed-tabs
    >
      <v-tab
        v-for="item in items"
      >
        <v-icon color="blue darken-3" style="padding-right: 8px;">{{ item.icon }}</v-icon>
        {{ item.header }}

      </v-tab>

      <v-tab>
        Recommended Products
      </v-tab>
    </v-tabs>

    {{selectedRegions}}

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="(value, name, index) in chartData" :key="index"><!--First Tab Content-->
        <v-card
          flat
        >

          <region-tab :chartData=value></region-tab>

        </v-card>
      </v-tab-item> <!--First Tab Content-->

      <!--Product Charts-->
      <region-products-tab :productsChartData=productsChartData></region-products-tab>

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
    chartData: null,
    productsChartData: null
  },

  data() {
    return {
      tab: null,
      items: [
        {
          header: 'At a Glance',
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
        }
        // ,
        // {
        //   header: 'Investment',
        //   icon: 'mdi-cash-multiple'
        // }
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
      })
    },
  },
  watch: {
    selectedRegions: function (newRegion) {
      console.log('n: ' + newRegion)
      this.getChartData(newRegion)
    }
  }
}
</script>

<style scoped>

</style>
