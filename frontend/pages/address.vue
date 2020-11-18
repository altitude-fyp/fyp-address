<template>
  <v-app>
    <div style="padding-top: 50px">
      <div class="parent">
          <div class="left">

            <!-- File Info -->
            <v-row>
              <h2 class="headerText">Input Address</h2>
            </v-row>
            
            <v-row>
              <div class="file">
                <h3> {{ addressFound }} </h3>                
              </div>
            </v-row><br/>

            <v-row>
              <span class="uploadDate">Last uploaded on {{ new Date().toLocaleString() }}</span>
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
                      <v-col>{{ this.housingType }}</v-col>
                      <v-col>{{ this.selectedRegions[0] }}</v-col>
                      <v-col>{{ this.selectedCountries[0] }}</v-col>
                    </v-row>

                  
                    <v-row class="atAGlanceSubHeader">
                      <v-col>Housing Type</v-col>
                      <v-col>Region</v-col>
                      <v-col>Country</v-col>
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

                      <!-- KEY FINANCIAL INDICATORS GOES HERE!!!! -->
                      <key-financial-indicators-analytics
                        :selectedCountries=selectedCountries>
                      </key-financial-indicators-analytics>

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

                      <tabs v-if="selectedRegions" :selected-regions="selectedRegions"/>

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
                     <analyticsResultDocs :address="postalCode" :endpoint="'/api/address'" :type="'address'"/> 
                  </v-expansion-panel-content>
                </v-expansion-panel>
                 
              </v-expansion-panels>
            </v-row>
          </div>

      <!--Google Maps-->
      <div class="right">
        <google-map-analytics
          :selectedRegions=selectedRegions
          />
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
import KeyFinancialIndicatorsAnalytics from "@/components/analytics/KeyFinancialIndicatorsAnalytics.vue"
import KeyFinancialIndicators from "@/components/home/GoogleBottomSheet/components/KeyFinancialIndicators.vue"
import tabs from "@/components/region/tabs"
import analyticsResultDocs from "@/components/apidocs/analyticsResultDocs"

export default {
  name: "address",
  components: {
    BarChart, lineChart, GoogleMapAnalytics,analyticsResultDocs,
    "country-statistics": CountryStatistics,
    "key-financial-indicators": KeyFinancialIndicators,
    "key-financial-indicators-analytics": KeyFinancialIndicatorsAnalytics
  },

  data() {
    return {
      selectedRegions: [],
      postalCode: null,
      housingType: null,
      addressFound: null,
      analyticsResult: {},
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
      countriesMetadata: null,
      chartData: null,
      tabs: null,
      panel: [0, 0],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },

    mounted() {
      this.housingType = this.$route.params.analytics_result.property_type.toLowerCase()
      this.selectedRegions.push(this.$route.params.analytics_result.region_found.toLowerCase())
      this.addressFound = this.$route.params.analytics_result.address_found
      this.postalCode = this.$route.params.address
      this.getEverything();

    },

    methods: {

      getEverything() {
        this.getCountryStatistics()
        this.getChartData()
        this.getCountriesMetadata()
      },

      getCountryStatistics() {
          // get statistics from aggregate.countries
          this.countryStatistics = null
          var url = process.env.BACKEND + "/api/countries/statistics/" + this.selectedCountries

          this.$axios.get(url).then((response) => {
              this.countryStatistics = response.data
          })
      },

      getCountriesMetadata() {
          // get flag, lat, lon, country code of each country in countries
          this.countriesMetadata = null
          var url = process.env.BACKEND + "/api/countries/metadata/" + this.selectedCountries[0]

          this.$axios.get(url).then((response) => {
              this.countriesMetadata = response.data
          })
      },

      getChartData() {
        this.chartData = null
        // this function gets chart data and stores in this.chartData
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
    text-transform:capitalize;
  }

  .atAGlanceSubHeader {
    text-align:center;
    font-size:14px;
    margin-top:-15px;
  }
</style>