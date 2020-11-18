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
                  sample_csv.csv
                </span>
                <div class="fileResults">
                  <span class="fileResultsSuccess">
                    {{ this.analyticsResult["valid_no"] }} records
                    <v-icon color="green">mdi-check</v-icon>
                  </span>
                  <span class="fileResultsError">
                    {{ this.analyticsResult["invalid_no"] }} records
                    <v-icon color="red">mdi-close</v-icon>
                  </span>
                  <span class="link">View
                  </span>
                </div>
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
                      <v-col>{{ this.analyticsResult["valid_no"] }}</v-col>
                      <v-col>{{ this.analyticsResult["no_of_region"] }}</v-col>
                      <v-col>{{ this.analyticsResult["most_region"] }}</v-col>

                    </v-row>
                    <v-row class="atAGlanceSubHeader">
                      <v-col>addresses in Singapore</v-col>
                      <v-col>regions</v-col>
                      <v-col>region with the highest no. of addresses</v-col>
                    </v-row>

                     <br/><v-divider></v-divider><br/>

                    <div class="housingTypeTitle" align="center"> <v-icon style="margin-bottom:5px;margin-right:5px;color:#d29a42">mdi-home</v-icon>Housing Type Breakdown</div>

                    <v-row class="atAGlanceHousingResults">
                      <v-col>{{ this.analyticsResult["hdb"] }}</v-col>
                      <v-col>{{ this.analyticsResult["private"] }}</v-col>
                      <v-col>{{ this.analyticsResult["others"] }}</v-col>
                    </v-row>

                    <v-row class="atAGlanceSubHeader">
                      <v-col>HDB</v-col>
                      <v-col>Private</v-col>
                      <v-col>Others</v-col>
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
import tabs from "@/components/region/tabs";

export default {
  name: "analytics",
  components: {
    BarChart, lineChart, GoogleMapAnalytics,
    "country-statistics": CountryStatistics,
    "key-financial-indicators-analytics": KeyFinancialIndicatorsAnalytics
  },

  data() {
    return {
      selectedRegions: null,
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
      chartData: null,
      tabs: null,
      panel: [0, 0],
      text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
    }
  },

    mounted() {
      // this.analyticsResult = JSON.parse(localStorage.getItem("analytics_result"))
      // this.analyticsResult = this.$router.params.analytics_result
      // console.log(this.analyticsResult)
      // this.analyticsResult = JSON.parse(JSON.stringify(this.$route.params.analytics_result))

      // console.log(this.$route.params.analytics_result)
      // console.log(typeof this.$route.params.analytics_result)

      // this.analyticsResult = this.$route.params.analytics_result
      this.analyticsResult["valid_no"] = this.$route.params.analytics_result.valid.total
      this.analyticsResult["invalid_no"] = this.$route.params.analytics_result.invalid.total
      this.analyticsResult["no_of_region"] = Object.keys(this.$route.params.analytics_result.valid.region_found).length
      this.analyticsResult["most_region"] = Object.keys(this.$route.params.analytics_result.valid.region_found)[0]
      this.analyticsResult["selectedRegions"] = Object.keys(this.$route.params.analytics_result.valid.region_found)
      this.analyticsResult["hdb"] = this.$route.params.analytics_result.valid.housing_type["HDB"]
      this.analyticsResult["private"] = this.$route.params.analytics_result.valid.housing_type["PRIVATE"]
      this.analyticsResult["others"] = this.$route.params.analytics_result.valid.housing_type["OTHERS"]

      this.selectedRegions = this.analyticsResult["selectedRegions"]

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
  }

  .atAGlanceHousingResults {
    text-align:center;
    font-size:30px;
    color:#d29a42;
    font-weight:700;
  }

  .atAGlanceSubHeader {
    text-align:center;
    font-size:14px;
    margin-top:-15px;
  }

  .housingTypeTitle {
    font-size:18px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:10px;
    color:#d29a42;
  }
</style>