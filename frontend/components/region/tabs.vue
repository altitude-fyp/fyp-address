<template>
  <v-container>
    <v-tabs
      v-model="tab"
      background-color="transparent"
      fixed-tabs
    >
      <v-tab
        v-for="item in items"
        :key="item"
      >
        <v-icon color="blue darken-3" style="padding-right: 8px;">{{item.icon}}</v-icon> {{ item.header }}

      </v-tab>
    </v-tabs>

    <v-tabs-items v-model="tab">
      <v-tab-item v-for="(value, name, index) in chartData" :key="index"><!--First Tab Content-->
        <v-card
          flat
        >

          <region-tab :chartData=value></region-tab>

        </v-card>
      </v-tab-item> <!--First Tab Content-->
      </v-tab-item>
    </v-tabs-items>
  </v-container>
</template>

<script>

import RegionTab from "@/components/region/components/RegionTab.vue"

export default {

  name: "tabs",

  components: {
    "region-tab": RegionTab,
    chartData: null
  },

  data() {
    return {
      tab: null,
      selectedRegions: "ang mo kio,bishan",
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
        this.getChartData()
      },
    
    getChartData() {
      // this function gets chart data and stores in this.chartData
      this.chartData = null
      var url = process.env.BACKEND + "/api/charts/regions/" + this.selectedRegions

      this.$axios.get(url).then((response) => {
        this.chartData = response.data.data
      })
    }
  }
}
</script>

<style scoped>

</style>
