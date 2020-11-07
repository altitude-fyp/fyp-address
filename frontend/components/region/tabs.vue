<template>

  <v-container>
    
    <div v-if=chartData>
      <v-tabs
        v-model=tab
        background-color="transparent"
        fixed-tabs>

        <!-- tabs go here -->
        <v-tab v-for="(item,i) in items"
          :key=i
          mandatory>

          <v-icon color="blue darken-3" style="padding-right: 8px;">{{item.icon}}</v-icon> {{ item.header }}

        </v-tab>

      </v-tabs>

      <!-- v tab items go here -->
      <v-tabs-items v-model=tab>

        <v-tab-item v-for="(value, key) in chartData" :key=key>
          
          <!--First Tab Content-->
          <v-card flat>
            <region-tab :chartData=value />
          </v-card>

        </v-tab-item> <!--First Tab Content-->

      </v-tabs-items>
    </div>

  </v-container>

</template>

<script>

import RegionTab from "@/components/region/components/RegionTab.vue"

export default {

  name: "tabs",

  props: ["selectedRegions"],

  components: {
    "region-tab": RegionTab,
  },

  data() {
    return {

      tab: 0,
      tabItem: 0,
      chartData: null,

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
