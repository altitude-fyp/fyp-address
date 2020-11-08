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
    </v-tabs>

    <!--   Will only load the tab when we have collected the data, resolve the empty 'At A Glance'-->
    <div v-if="isLoaded">
      <v-tabs-items v-model="tab">

        <v-tab-item v-for="(value, name, index) in chartData" :key="index"><!--First Tab Content-->
          <v-card
            flat
          >
            <region-tab :chartData=value></region-tab>
          </v-card>
        </v-tab-item> <!--First Tab Content-->

        <!--      </v-tab-item>-->
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
    chartData: null,
  },

  data() {
    return {
      tab: null,
      isLoaded: false,
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
