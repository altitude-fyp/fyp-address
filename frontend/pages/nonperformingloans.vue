<template>
  <v-app>
    <div class="searchCountry">
      <v-parallax 
        height="320"
        :src="require('../images/npl_bg.png')">
      </v-parallax>
    <v-container style="margin-top:-50px; margin-bottom:-80px">
      <!-- Search Country -->
      <v-row justify="center">
          <v-col cols="11">
          <v-autocomplete class="elevation-0"
            v-model="value"
            :items="items"
            rounded
            solo
            label="Enter country name"
          ></v-autocomplete>
          </v-col>

        <v-col cols="1">
        <div style="margin-top:5px">
        <v-btn
          depressed
          color="primary"
        >
          Search
        </v-btn>
        </div>
        </v-col>
      </v-row>
      
    </v-container>
    </div>
    <!-- Search Country -->
    <div style="padding-top: 50px">
        <v-container>
            <v-row>
                <img src="https://www.countryflags.io/sg/flat/64.png" style="height:40px;margin-right:10px;"/>
                <h2 class="headerText">Singapore</h2>

                <v-spacer></v-spacer>
                <!-- Forecast -->
                  <img :src="require('../images/up_arrow.png')" style="height:20px;margin-top:10px;margin-right:15px"/>
                  <span style="margin-top:10px;font-weight:700">2021 Forecast</span>
                
            </v-row>

            <v-row v-for="i in 2" :key=i>
              <v-col v-for="j in 5" cols="2.4" :key=j>
                <span class="featureName">Feature Name</span><br/>
                <span class="similarityScore">Similarity Score</span>
              </v-col>
            </v-row>

              <npl-country-chart
                  :chartData=chartData>
              </npl-country-chart>

            <br/><v-divider></v-divider><br/>

            <v-row>
              <h2 class="headerText">Top 10 & Bottom 10 Countries</h2>
            </v-row>

            <v-row>
              <npl-top10-chart
                  :top10ChartData=top10ChartData>
              </npl-top10-chart>
            </v-row>

            <v-row>
              <v-toolbar elevation="0">
                <v-tabs
                  v-model="tabs"
                  
                >
                  <v-tabs-slider></v-tabs-slider>
                  <v-tab
                    href="#tab-1"
                    class="primary--text"
                  >
                    <v-icon>mdi-phone</v-icon>
                  </v-tab>

                  <v-tab
                    href="#tab-2"
                    class="primary--text"
                  >
                    <v-icon>mdi-heart</v-icon>
                  </v-tab>
                </v-tabs>
              </v-toolbar>

              <v-tabs-items v-model="tabs">
                <v-tab-item
                  v-for="i in 2"
                  :key="i"
                  :value="'tab-' + i"
                >
                  <v-card flat>
                    <v-card-text v-text="text"></v-card-text>
                  </v-card>
                </v-tab-item>
              </v-tabs-items>
            </v-row>

        </v-container>
    </div>
  </v-app>
</template>

<script>
import lineChart from "@/components/analytics/lineChart";
import barChart from "@/components/analytics/barChart";
import CountryStatistics from "@/components/analytics/CountryStatisticsAnalytics.vue"
import NPLCountryChart from "@/components/nonperformingloans/NPLCountryChart.vue"
import NPLTop10Chart from "@/components/nonperformingloans/NPLTop10Chart.vue"

  export default {
    components: {
      "npl-country-chart": NPLCountryChart,
      "npl-top10-chart": NPLTop10Chart
    },
    data: () => ({
      items: ['Angola', 'Australia', 'Canada', 'Chad', 'Comoros', 'Dominica', 'Equatorial Guinea', 'Estonia', 'Greece', 'Hong Kong', 'Luxembourg', 'Macao', 'Norway', 'Saint Kitts and Nevis', 'San Marino', 'Sweden', 'Switzerland', 'Tajikistan', 'Ukraine', 'United States'],
      values: ['Angola', 'Australia', 'Canada', 'Chad', 'Comoros', 'Dominica', 'Equatorial Guinea', 'Estonia', 'Greece', 'Hong Kong', 'Luxembourg', 'Macao', 'Norway', 'Saint Kitts and Nevis', 'San Marino', 'Sweden', 'Switzerland', 'Tajikistan', 'Ukraine', 'United States'],
      value: null,
      selectedCountries: ["Singapore"],
      countryStatistics: null,
      selectedCountryStatisticsFeatures: [
          "gdp nominal",
          "unemployment rate",
          "Financial Development Index",
          "population density",
          "literacy rate",
          "life expectacy (overall)",
          "gini",
          "Consumer Price Index, All items",
      ],
      chartData: null,
      top10ChartData: null,
      tabs: null,
      panel: [0, 0],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }),

    mounted() {
    this.getEverything();
  },

  methods: {

      getEverything() {
        this.getChartData()
        this.getTop10Chart()
      },

      //Bank nonperforming loans to total gross loans chart
      getChartData() {
        // this function gets chart data and stores in this.chartData
        this.chartData = null
        var url = process.env.BACKEND + "/api/analytics/npl_charts/" + this.selectedCountries

        this.$axios.get(url).then((response) => {
            this.chartData = response.data.charts
        })
      },

      getTop10Chart() {
        // this function gets chart data and stores in this.chartData
        this.top10ChartData = null
        var url = process.env.BACKEND + "/api/analytics/sorted_npl_data/"

        this.$axios.get(url).then((response) => {
            this.top10ChartData = response.data.charts
        })
      },
  }
  }
</script>

<style scoped>

  .searchCountry {
    background-color: #f5f5f5;
  }

  .v-expansion-panel::before {
   box-shadow: none !important;
  }

  .v-expansion-panel-header {
   padding:0;
   margin-top:20px;
   margin-bottom:20px;
  }

  .v-expansion-panel-content >>> .v-expansion-panel-content__wrap {
    padding:0 15px 0 0;
    margin-bottom:25px;
  }

  .featureName{
    color:#454545 !important;
    font-weight:700;
    font-size:16px;
    padding:16px;
  }

  .similarityScore{
    color:#454545 !important;
    font-size:14px;
    padding:16px;
  }

  .charts {
    box-shadow: none !important;
    padding-left:10px;
    padding-right:10px;
  }

  .chartsTitle{
    color:#d29a42;
    margin-bottom:10px;
    text-align:center;
  }

  .chartsDescription {
    font-size:13px;
    padding-left:10px;
    padding-right:10px;
  }

  .uploadDate {
    color:#5a5a5a;
    font-size:12px;
  }

  .link {
    color:#215085;
    font-size:14px;
    font-weight:700;
  }

  .headerText {
    color:#215085;
    margin-bottom:10px;
  }

</style>