<template>
  <v-app v-if="isLoaded">
    <div style="padding-top: 50px">
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
              <v-expansion-panels 
                accordion 
                v-model="panel"
                multiple
              >
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="22"
                      max-width="22"
                      :src="require('../images/icons/ataglance.png')"
                    ></v-img>
                    <h2>At a Glance</h2>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </v-expansion-panel-content>
                </v-expansion-panel>

                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="22"
                      max-width="22"
                      :src="require('../images/icons/globe.png')"
                    ></v-img>
                    <h2>Singapore</h2>
                  </v-expansion-panel-header>
                  <v-expansion-panel-content>
                    
                    <!--Top 8 features-->
                    <v-row v-for="x in 2">
                      <v-col v-for="n in 4">
                        <v-row>
                            <v-card-subtitle class="featuresTitle"> {{ Tags.data.top8[(4*(x-1)+n)-1].name }}</v-card-subtitle>
                            <v-card-text style="font-size: 16px;">{{ formatValue(Tags.data.top8[(4*(x-1)+n)-1].value) }}</v-card-text>   
                        </v-row>
                      </v-col>
                    </v-row>
                    <!--Top 8 features-->

                    <!-- Chart -->
                    <h3>Key Financial Indicators</h3>
                    <v-card class="mx-auto charts">
                      <v-container>
                        <v-row> 
                          <v-col v-for="data in chartdata" cols="6">
                            <v-row>
                              <v-col>
                              <div class="chartsTitle">
                                  <h3>{{data.title}}</h3>
                              </div>
                                <div class="charts">
                                  <line-chart
                                    v-if="isChartLoaded"
                                    :chartdata="data"
                                  />
                                </div>
                                <br/>
                                <p class="chartsDescription">{{data.description}}</p>
                              </v-col>
                            </v-row>
                          </v-col>
                        </v-row>
                      </v-container>
                    </v-card>
                    <!-- Chart -->
                  </v-expansion-panel-content>
                </v-expansion-panel>

                <!--Region Data in Country-->
                <v-expansion-panel>
                  <v-expansion-panel-header>
                    <v-img class="analyticsIcons"
                      max-height="22"
                      max-width="22"
                      :src="require('../images/icons/region.png')"
                    ></v-img>
                    <h2>Regions in Singapore</h2>
                  </v-expansion-panel-header>
                  
                  <v-expansion-panel-content>                    
                    <v-toolbar flat>
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
                            <span class="regionTabText">At a Glance</span>
                          </v-tab>

                          <v-tab
                            href="#tab-2"
                            class="primary--text"
                          >
                            <v-icon>mdi-heart</v-icon>
                            <span class="regionTabText">Economy</span>
                          </v-tab>

                          <v-tab
                            href="#tab-3"
                            class="primary--text"
                          >
                            <v-icon>mdi-account-box</v-icon>
                            <span class="regionTabText">Society</span>
                          </v-tab>

                          <v-tab
                            href="#tab-4"
                            class="primary--text"
                          >
                            <v-icon>mdi-account-box</v-icon>
                            <span class="regionTabText">Household</span>
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
                <!--Region Data in Country-->

              </v-expansion-panels>
            </v-row>
            <br/><br/>
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
import axios from 'axios';
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";
import GoogleMapAnalytics from "@/components/home/GoogleMapAnalytics";

export default {
  name: "analytics",
  components: {BarChart, lineChart, GoogleMapAnalytics},

  data: () => ({
    loaded: false,
    chartdata: {},
    panel: [0, 1],
    isLoaded: false,
    tabs: null,
    Tags: null,
    chartdata: [],
    isLoaded: false,
    isChartLoaded: false,
    data: null,
    countries: ['Singapore'],
    text: 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
  }),

  mounted() {
    this.getEverything(["Singapore"]);
  },

    methods: {
    formatValue(num) {
      return Math.abs(Number(num)) >= 1.0e+9

      ? (Math.abs(Number(num)) / 1.0e+9).toFixed(2) + " billion"

      : Math.abs(Number(num)) >= 1.0e+6

      ? (Math.abs(Number(num)) / 1.0e+6).toFixed(2) + " million"

      : +(Math.round(num + "e+4")  + "e-4");
    },

    topThreeOnClose(country_name) {

      // this function is called when the user clicks any of the flags in the top 3 countries section

      this.getEverything([country_name])
    },

    onClose(acceptance) {

      // this function is called when the user selects the countries that he wants to analyze

      this.countries = acceptance[1]
      this.chartdata = null
      this.getEverything(this.countries)
    },

    getEverything(countries) {

      this.countries = countries

      // GETTING COUNTRY DATA
      this.$axios.$post(process.env.BACKEND + '/api/countries/', {
          "countries": countries
        }
      ).then((Tags) => {
        this.Tags = Tags
        console.log(this.Tags)
        this.isLoaded = true
        this.$emit('load-coordinates', this.Tags.data.coordinates)
      })

      // GETTING CHARTS DATA FOR COUNTRY
      this.$axios.$post( process.env.BACKEND + '/api/charts/', {
        "countries": countries

      }).then((response) => {

        this.chartdata = response.data.items
        this.isChartLoaded = true
      })

      // GETTING TOP3 COUNTRIES ONLY IF LEN(COUNTRIES) == 1
      if (countries.length == 1) {
        this.$axios.$get( process.env.BACKEND + '/api/analytics/top_countries/' + countries[0]).then((topThree) => {

            this.topThree = topThree
            this.getTopThree = true
          }
        ) 
      } else {
        this.getTopThree = false
      }

      this.$axios.$post( process.env.BACKEND + '/api/csv/', {
        "countries": countries

      }).then((data) => {
          this.csvdata = data
          this.getCsvData = true
        }
      )

    },
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
</style>