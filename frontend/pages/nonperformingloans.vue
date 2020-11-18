<template>
  <v-app>
    <div class="searchCountry">
      <v-parallax 
        height="320"
        :src="require('../images/npl_bg.png')">
      </v-parallax>

      <v-container style="margin-top:-50px; margin-bottom:-80px">

        <!-- Search Country -->
        <npl-country-selection
            @submitSelectedCountriesEvent="updateSelectedCountries">
        </npl-country-selection>
        <!-- Search Country -->
      
      </v-container>
    </div>

    <div v-if="selectedCountry && countriesMetadata && countryStatistics" style="padding-top: 50px">
        <v-container>

            <v-row v-if="countriesMetadata[selectedCountry] && countriesMetadata[selectedCountry]['flag']">
              <img :src="countriesMetadata[selectedCountry]['flag']" style="height:40px;margin-right:10px;" contain/>
              <h2 class="headerText">{{ selectedCountry}}</h2>

              <v-spacer></v-spacer>

                <!-- Country Forecast -->
                <div v-if="countryForecast[selectedCountry] === 0">
                  <img :src="require('../images/down_arrow.png')" class="forecastArrow"/>
                </div>

                <div v-else>
                  <img :src="require('../images/up_arrow.png')" class="forecastArrow"/>
                </div>

                <span style="margin-top:8px;font-weight:700">2021 Forecast</span>
                <!-- Country Forecast -->
            </v-row>

            <br/>

            <!-- Top 10 Features -->
            <v-row>
              <div class="top10FeaturesText">
                <h3>Top 10 Features</h3>
              </div>
            </v-row>
            <v-row v-for="i in 2" :key=i>
                <v-col v-for="feature in countryStatistics[selectedCountry].slice((i-1)*5,5*(i))" :key="feature.name">
                  <div align="center">
                    <span class="featureName">{{feature.name}}</span> <br/>
                    <span class="similarityScore">{{formatValue(feature.score)}}</span>
                  </div>
                </v-col>
            </v-row>
            <!-- Top 10 Features -->

            <!-- Country NPL Chart -->
            <npl-country-chart
                :chartData=chartData>
            </npl-country-chart>
            <!-- Country NPL Chart -->

            <br/><v-divider></v-divider><br/>

            <!-- Top & Bottom 10 -->
            <v-row>
              <h2 class="headerText">Top 10 & Bottom 10 Countries</h2>
            </v-row>
            <npl-top10-chart
                :top10ChartData=top10ChartData>
            </npl-top10-chart>
            <!-- Top & Bottom 10 -->

        </v-container>
    </div>
  </v-app>
</template>

<script>
import lineChart from "@/components/analytics/lineChart";
import barChart from "@/components/analytics/barChart";
import NPLCountryChart from "@/components/nonperformingloans/NPLCountryChart.vue"
import NPLTop10Chart from "@/components/nonperformingloans/NPLTop10Chart.vue"
import CountrySelection from "@/components/nonperformingloans/CountrySelection.vue"

export default {
  components: {
    "npl-country-chart": NPLCountryChart,
    "npl-top10-chart": NPLTop10Chart,
    "npl-country-selection": CountrySelection,
  },
  data: () => ({
    value: null,
    selectedCountry: "Singapore",
    countryStatistics: null,
    chartData: null,
    top10ChartData: null,
    forecastValue: 1,
    countriesMetadata: null,
    selectedFeatures: [],
  }),

  mounted() {
    console.log(process.env.BACKEND)
    this.getEverything();
  },

  methods: {

      getEverything() {
        this.getCountriesMetadata()
        this.getChartData()
        this.getTop10Chart()
        this.getCountryStatistics()
        this.getCountryForecast()
      },

      getCountriesMetadata() {
            // get flag, lat, lon, country code of each country in countries
            this.countriesMetadata = null
            var url = process.env.BACKEND + "/api/countries/metadata/" + this.selectedCountry

            this.$axios.get(url).then((response) => {
                this.countriesMetadata = response.data
            })
        },

      //Bank nonperforming loans to total gross loans chart
      getChartData() {
        // this function gets chart data and stores in this.chartData
        this.chartData = null
        var url = process.env.BACKEND + "/api/analytics/npl_charts/" + this.selectedCountry

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

      getCountryStatistics() {
          // get statistics from aggregate.countries
          this.countryStatistics = null
          var url = process.env.BACKEND + "/api/analytics/npl_country_features/" + this.selectedCountry

          this.$axios.get(url).then((response) => {
              this.countryStatistics = response.data
          })
      },

      getCountryForecast() {
          // get country forecast
          this.countryForecast = null
          var url = process.env.BACKEND + "/api/analytics/npl_forecast"

          this.$axios.get(url).then((response) => {
              this.countryForecast = response.data
          })
      },

      updateSelectedCountries(selectedCountry) {
        //this function is called after user submits his selected countries from the country selection dialog
        this.selectedCountry = selectedCountry
        this.getEverything()
      },

      formatValue(num) {
          return Math.abs(Number(num)) >= 1.0e+9

          ? (Math.abs(Number(num)) / 1.0e+9).toFixed(2) + " billion"

          : Math.abs(Number(num)) >= 1.0e+6

          ? (Math.abs(Number(num)) / 1.0e+6).toFixed(2) + " million"

          : +(Math.round(num + "e+4")  + "e-4");
      },
  }
  }
</script>

<style scoped>

  .searchCountry {
    background-color: #f5f5f5;
  }

  .featureName{
    color:#454545 !important;
    font-size:14px;
    padding:16px;
  }

  .similarityScore{
    color:#215085 !important;
    font-weight:700;
    font-size:20px;
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
    margin-bottom:5px;
  }

  .top10FeaturesText {
    color:#d29a42;
    margin-bottom:10px;
    text-align:center;
    margin:0 auto;
  }

  .forecastArrow {
    height:20px;
    margin-top:10px;
    margin-right:15px
  }

</style>