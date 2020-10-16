<template>
  <v-app>
    <div style="padding-top: 20px">
      <div class="parent">
      <div class="left">
        <v-row>
          <h2>File Info</h2>
        </v-row>

        <v-row>
          <div class="file">
            <div class="fileName">
              address_SG_14102020.csv
            </div>
            <div class="fileResults">
              <div class="fileResultsSuccess">
                418 records
                <v-icon color="green">mdi-check</v-icon>
              </div>
              <div class="fileResultsError">
                418 records
                <v-icon color="red">mdi-close</v-icon>
              </div>
            </div>
          </div>
        </v-row>

        <br/><v-divider></v-divider><br/>

        <v-row>
          <h2>Address data</h2>
          <v-expansion-panels accordion>
            <v-expansion-panel>
              <v-expansion-panel-header>
                <h3>At a Glance</h3>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
              </v-expansion-panel-content>
            </v-expansion-panel>

            <v-expansion-panel>
              <v-expansion-panel-header>
                <h3>Country Level</h3>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-row>

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
      </div>

      <div class="right">
      <div class="map">
        <google-map :coordinates="coordinates"/>
      </div>
      </div>
    </div>
    </div>
  </v-app>

</template>

<script>
import axios from 'axios';
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";
import GoogleMapAnalytics from "@/components/home/GoogleMapAnalytics";

export default {
  name: "analytics",
  components: {BarChart, lineChart, GoogleMapAnalytics},

  data: () => ({
    country: "Singapore",
    country1: "Japan",
    country2: "Australia",
    loaded: false,
    chartdata: {}
  }),

  async created() {
    this.loaded = false
    try {
      // const response = await axios.get( process.env.BACKEND + '/api/charts/'  + this.country)
      const req = {
        "countries": [
          this.country, this.country1, this.country2
        ]
      }
      const response = await axios.post( process.env.BACKEND + '/api/charts/', req)

      // this.chartdata = JSON.parse(JSON.stringify(response.data))
      this.chartdata = response.data.data.items
      console.log(this.chartdata)
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
};
</script>

<style scoped>
  .file {
    width:600px;
    margin-top:15px;
  }
  .fileName {
    float:left;
  }

  .fileResults {
    float:right;
    margin:0 auto;
  }

  .fileResultsSuccess {
    margin-right:30px;
  }

  .fileResultsError {
    margin:0 auto;
  }

  .successDot {
    height: 25px;
    width: 25px;
    background-color: #4BB543;
    border-radius: 50%;
    display: inline-block;
  }

  .parent {
    margin: 0;
    width: 100%;
    background-color: #EBEBEB;
  }

  .left {
      float: left;
      width: 60%;
      height: 100%;
  }

  .right {
    position: fixed;
    top: 0%;
    height: 100%;
    margin: 0;
    padding: 0;
  }

  .map {
    width: 40%;
    position: fixed;
    right:0px;
    height:100%;
    overflow:hidden;
  }
</style>
