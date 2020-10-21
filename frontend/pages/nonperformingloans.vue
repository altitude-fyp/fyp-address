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
            clearable
            filled
            rounded
            solo
            label="Enter country name"
          ></v-autocomplete>
          </v-col>

        <v-col cols="1">
        <v-btn
          depressed
          color="primary"
        >
          Search
        </v-btn>
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

                  </v-expansion-panel-content>
                </v-expansion-panel>
              </v-expansion-panels>
            </v-row>
        </v-container>
    </div>
  </v-app>
</template>

<script>
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";
import CountryStatistics from "@/components/analytics/CountryStatisticsAnalytics.vue"
import NPLCountryChart from "@/components/nonperformingloans/NPLCountryChart.vue"

  export default {
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
    }),

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