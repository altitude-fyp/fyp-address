<template>
  <!--fluid style="padding-top: 400px; padding-left: 240px; position:absolute; z-index: 1;"-->
  <v-container>
    <v-row style="margin-bottom: -20px">
      <!--Select US or Singapore button-->
      <v-col cols="2" style="padding-top: 20px;">
        <v-select
          v-model="preselect"
          :items="items"
          menu-props="auto"
          label="Country"
          hide-details
          prepend-icon="mdi-map"
          outlined
          dense
        ></v-select>
      </v-col>

      <!--Address Search Bar-->
      <v-col cols="8">
        <v-text-field
          v-model="address"
          prepend-inner-icon="mdi-magnify"
          placeholder="Enter a postal code, hit 'Enter' to search"
          v-on:keypress.enter="lookUpAddress"
        >
        </v-text-field>
      </v-col>

      <!--upload CSV button-->
      <v-col cols="2" style="padding-top: 20px;">

        <v-file-input
          placeholder="Upload CSV"
          v-model="csv"
          accept=".csv"
          dense
          @change="csvAccept">

        </v-file-input>

        <!-- <v-icon >mdi-upload</v-icon> -->

      </v-col>
    </v-row>

    <!-- Switch to Region View -->
    <v-row style="margin-bottom: -50px">
      <v-col align="right">
      <v-btn
        outlined
        color="#004D8E"
        width="240"
        to="/region"
      >
        <v-icon left>mdi-eye</v-icon>
        Switch to Region View
      </v-btn>
      </v-col>
    </v-row>


  </v-container>

</template>

<script>

import Papa from 'papaparse'

export default {
  name: "CSVSearch",
  components: {
    Papa,
  },
  data() {
    return {
      preselect: 'Singapore',
      address: '',
      items: ['Singapore', 'USA'],
      csv: null,
      data: null,
    }
  },
  methods: {

    lookUpAddress() {

      let url = process.env.BACKEND + "/api/address/frontend/"
      this.$axios.post(url, {"address": this.address}).then((response) => {
        localStorage.setItem("analytics_result", JSON.stringify(response["data"]["data"]))
        
        // this.$router.push({path: '/analytics', params: { analytics_result: response }})
        console.log(response)
        
        this.$router.push({name: 'address', params: { analytics_result: response["data"]["data"], address: this.address }})

      }) 

    },

    csvAccept() {

      Papa.parse(this.csv, {

        delimiter: ",",
        header: true,

        complete: (results) => {
          // this function is called when papaparse finishes parsing the CSV
          // this function sends the CSV data to the backend
          let url = process.env.BACKEND + "/api/address/frontend/csv/"
          this.$axios.post(url, {"addresses": results.data}).then((response) => {
            localStorage.setItem("analytics_result", JSON.stringify(response["data"]))
            
            // this.$router.push({path: '/analytics', params: { analytics_result: response }})
            
            this.$router.push({name: 'analytics', params: { analytics_result: response["data"]["data"] }})
  
          }) 
        }
      });
    }
  }

}
</script>

<style scoped>

</style>

