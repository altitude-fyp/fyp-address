<template>
  <v-app>
    <div style="padding-top: 50px">

    {{ info }}

      <v-container>
        
        <v-row dense>
          <v-col>
            <v-card>
              <line-chart
                v-if="loaded"
                :chartdata="chartdata[0]"
              />
            </v-card>
          </v-col>

          <v-col>
            <v-card>
              <line-chart
                v-if="loaded"
                :chartdata="chartdata[1]"
              />
            </v-card>
          </v-col>
        </v-row>

        <!-- ############################ -->

         <v-row dense>
          <v-col>
            <v-card>
              <line-chart
                v-if="loaded"
                :chartdata="chartdata[2]"
              />
            </v-card>
          </v-col>

          <v-col>
            <v-card>
              <line-chart
                v-if="loaded"
                :chartdata="chartdata[3]"
              />
            </v-card>
          </v-col>
        </v-row>

      </v-container>


    </div>
  </v-app>

</template>

<script>
import axios from 'axios';
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";

export default {
  name: "analytics",
  components: {BarChart, lineChart},

  data: () => ({
    country: "Singapore",
    loaded: false,
    chartdata: {}
  }),

  async created() {
    this.loaded = false
    try {
      // const response = await axios.get('http://lzl.blue/api/charts/'  + this.country)
      const req = {
        "countries": [
          this.country
        ]
      }
      const response = await axios.post('http://localhost:8000/api/charts/', req)

      // this.chartdata = JSON.parse(JSON.stringify(response.data))
      this.chartdata = response.data.data.items
      console.log(this.chartdata)
      console.log(this.loaded)
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }

};
</script>

<style scoped>

</style>
