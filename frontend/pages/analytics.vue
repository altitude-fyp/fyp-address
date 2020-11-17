<template>
  <v-app>
    <div style="padding-top: 50px">
      <div class="parent">
          <div class="left">

            <!-- File Info -->
            <v-row>
              <h2 class="headerText">File Info</h2>
            </v-row>
            
            <v-row>
              <div class="file">
                <span class="fileName">
                  address_SG_14102020.csv
                </span>
                <div class="fileResults">
                  <span class="fileResultsSuccess">
                    418 records
                    <v-icon color="green">mdi-check</v-icon>
                  </span>
                  <span class="fileResultsError">
                    23 records
                    <v-icon color="red">mdi-close</v-icon>
                  </span>
                  <span class="link">View
                  </span>
                </div>
              </div>
            </v-row><br/>

            <v-row>
              <span class="uploadDate">Last uploaded on 18 October 2020, 07:30 AM</span>
            </v-row>
            <!-- File Info -->

            <br/><v-divider></v-divider><br/>

            <v-row>

              <h2 class="headerText">Address data</h2>
              
              <v-expansion-panels 
                accordion 
                v-model="panel"
                multiple>

                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="18"
                      max-width="18"
                      :src="require('../images/icons/ataglance.png')"
                    ></v-img>
                    <h3>At a Glance</h3>
                  </v-expansion-panel-header>

                  <v-expansion-panel-content>
                    <v-row class="atAGlanceResults">
                      <v-col>Test</v-col>
                      <v-col>10</v-col>
                      <v-col>Toa Payoh</v-col>
                    </v-row>
                    <v-row class="atAGlanceSubHeader">
                      <v-col>Singapore</v-col>
                      <v-col>regions</v-col>
                      <v-col>region with the highest no. of addresses</v-col>
                    </v-row>
                  </v-expansion-panel-content>
                </v-expansion-panel>

                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="18"
                      max-width="18"
                      :src="require('../images/icons/globe.png')"
                    ></v-img>
                    <h3>Singapore</h3>
                  </v-expansion-panel-header>

                  <v-expansion-panel-content>
                      <country-statistics
                          :countriesMetadata="{1:1}"
                          :countryStatistics=countryStatistics
                          :selectedCountries=selectedCountries
                          :selectedFeatures=selectedCountryStatisticsFeatures>
                      </country-statistics>

                      <key-financial-indicators
                        :chartData=chartData>
                      </key-financial-indicators>
                  </v-expansion-panel-content>
                </v-expansion-panel>

                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="18"
                      max-width="18"
                      :src="require('../images/icons/region.png')"
                    ></v-img>
                    <h3>Regions in Singapore</h3>
                  </v-expansion-panel-header>

                  <v-expansion-panel-content>
                    <v-toolbar elevation="0">
                      <v-tabs
                        v-model="tabs"
                        fixed-tabs
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

                        <v-tab
                          href="#tab-3"
                          class="primary--text"
                        >
                          <v-icon>mdi-account-box</v-icon>
                        </v-tab>

                        <v-tab
                          href="#tab-4"
                          class="primary--text"
                        >
                          <v-icon>mdi-account-box</v-icon>
                        </v-tab>

                      </v-tabs>
                    </v-toolbar>

                    <v-tabs-items v-model="tabs">
                      <v-tab-item
                        v-for="i in 4"
                        :key="i"
                        :value="'tab-' + i"
                      >
                        <v-card flat>
                          <v-card-text v-text="text"></v-card-text>
                        </v-card>
                      </v-tab-item>
                    </v-tabs-items>
                  </v-expansion-panel-content>
                </v-expansion-panel>

                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="18"
                      max-width="18"
                      :src="require('../images/icons/code.png')"
                    ></v-img>
                    <h3>Code Snippet</h3>
                  </v-expansion-panel-header>

                  <v-expansion-panel-content>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </v-expansion-panel-content>
                </v-expansion-panel>              
              </v-expansion-panels>
            </v-row>
          </div>

      <!--Google Maps-->
      <div class="right">
        <google-map-analytics :coordinates="coordinates"/>
      </div>
      <!--Google Maps-->
      </div>
    </div>
  </v-app>
</template>

<script>
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";
import GoogleMapAnalytics from "@/components/home/GoogleMapAnalytics";
import CountryStatistics from "@/components/analytics/CountryStatisticsAnalytics.vue"
import KeyFinancialIndicators from "@/components/analytics/KeyFinancialIndicatorsAnalytics.vue"

export default {
  name: "analytics",
  components: {
    BarChart, lineChart, GoogleMapAnalytics,
    "country-statistics": CountryStatistics,
    "key-financial-indicators": KeyFinancialIndicators,
    },

  data() {
    return {
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
      tabs: null,
      panel: [0, 0],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },

    mounted() {
      this.getEverything();
    },

    methods: {

      getEverything() {
        this.getCountryStatistics()
        this.getChartData()
      },

      getCountryStatistics() {
          // get statistics from aggregate.countries
          this.countryStatistics = null
          var url = process.env.BACKEND + "/api/countries/statistics/" + this.selectedCountries

          this.$axios.get(url).then((response) => {
              this.countryStatistics = response.data
          })
      },

      getChartData() {
        // this function gets chart data and stores in this.chartData
        this.chartData = null
        var url = process.env.BACKEND + "/api/charts/" + this.selectedCountries

        this.$axios.get(url).then((response) => {
            this.chartData = response.data.charts
        })
      },
  }

}

</script>

<style scoped>
  .file {
    width:700px;
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
    padding-right:40px;
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
  }

  .left {
      float: left;
      width: 60%;
      height: 100%;
      padding-left:50px;
      padding-right:30px;
  }

  .right {
    position: fixed;
    top: 0%;
    height: 100%;
    margin: 0;
    padding: 0;
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

  .analyticsIcons {
    margin-right:10px;
  }

  .regionTabText {
    text-transform: none !important;
    margin-left: 10px;
    font-size:16px;
  }

  .featuresTitle{
    color:#215085 !important;
    font-weight:700;
    font-size:16px;
    padding:16px;
  }

  .charts  {
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
  }
  
  .atAGlanceResults {
    text-align:center;
    font-size:30px;
    color:#215085;
    font-weight:700;
  }

  .atAGlanceSubHeader {
    text-align:center;
    font-size:14px;
    margin-top:-15px;
  }
</style>