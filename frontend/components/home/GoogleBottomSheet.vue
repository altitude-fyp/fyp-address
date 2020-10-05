<template>
  <v-container v-if="isLoaded">
    <v-row>
      <v-col cols="3">

        <v-card
          class="mx-auto"
          outlined
        >
          <div v-if='countries.length === 1'>
            <v-row class="mx-auto">
              <v-col class="mx-auto">
                <div class="sidebarCountryName">{{ countries[0] }}</div>
              </v-col>
            </v-row>
            <v-row>
              <div class="countryFlagSidebarSection">
                <img class="countryFlagSidebar" :src="Tags.data.flag[0]" aspect-ratio="2" contain/>
              </div>
            </v-row>

          </div>
          <div v-else>
            <div v-for="flagAccess in Tags.data.flag">
              <v-row class="mx-auto">
                <v-col class="mx-auto">
                  <div class="sidebarCountryName">
                    {{ countries[Tags.data.flag.indexOf(flagAccess)] }}
                  </div>
                </v-col>
              </v-row>
              <v-row>
                <div class="countryFlagSidebarSection">
                  <img class="countryFlagSidebar" :src="flagAccess" aspect-ratio="2" contain/>
                </div>
              </v-row>
            </div>
          </div>

          <!--v-row class="mx-auto">
            <v-col>
              <div class="overline mb-4" v-if="access==='Region'">
                REGION COMES HERE
              </div>
            </v-col>
          </v-row>-->

          <v-col>
            <!-- <div v-if="countries.length === 1">
              <v-row style="padding-bottom: 8px;" justify="center">
                <v-btn small outlined color="primary" @click="dialog = true, access= 'Region'">Select Regions in
                  {{ countries[0] }}
                </v-btn>
              </v-row>
            </div> -->

            <v-row justify="center">
              <v-btn @click="dialog = true, access= 'Countries'"
                color="#004D8E"
                class="white--text mb-2 sidebar"
                depressed
              >Countries to Compare
              </v-btn>
            </v-row>

            <v-row justify="center">
              <vue-json-to-csv :json-data="csvdata" :csv-title="'countries_data'">
                <v-btn
                  outlined
                  color="#004D8E"
                  class="mb-2 sidebar"
                  depressed
                ><v-icon style="margin-right:5px">mdi-download</v-icon>Download CSV
                </v-btn>
              </vue-json-to-csv>
            </v-row>
          </v-col><!-- Region/Country btn-->
          <v-divider></v-divider>

          <br/>
          <v-list
            subheader
            flat
          >
            <v-list-item-group
              v-model="selectTags"
              multiple
            >
              <v-row style="padding-top: 8px;" justify="center">
                <v-btn @click="selectTags = []"
                  outlined
                  color="#004D8E"
                  class="mb-2"
                  depressed
                >Clear Filter
                </v-btn>
              </v-row> <!--Clear Filter btn-->
              <br/>
              <div class="filtersSection">
                <div v-for="item in Tags.data.filter">
                  <div class="filtersSectionTag">{{ item.category }}</div>
                  <div v-for="tag in item.value">
                    <v-list-item>
                      <template v-slot:default="{ active }">
                        <v-list-item-action>
                          <v-checkbox
                            :input-value="active"
                            color="primary"
                          ></v-checkbox>
                        </v-list-item-action>

                        <v-list-item-content>
                          <v-list-item-title>{{ tag }}</v-list-item-title>
                        </v-list-item-content>

                      </template>

                    </v-list-item>
                  </div>
                </div>
              </div>

            </v-list-item-group>
          </v-list> <!--Filter data checklist-->

        </v-card>

      </v-col>
      <v-col cols="9">
        <h2 class="sectionTitle">Country Statistics</h2>
        <v-card class="mx-auto">
          <v-container>

            <!--Top 8 features-->
            <v-row v-for="x in 2">
              <v-col v-for="n in 4" cols="3">
                <v-row>
                  <v-col v-if="selectTags.length < 4*(x-1)+n">
                    <v-card-subtitle class="featuresTitle"> {{ Tags.data.top8[(4*(x-1)+n)-1].name }}</v-card-subtitle>
                      <!-- Loop to show the flag  -->
                      <div v-for="(flag, i) in Tags.data.flag" class="countryFlagIndicators">
                        <img align="left" class="countryFlag" :src="Tags.data.flag[i]" aspect-ratio="2" contain/>
                        <v-card-text style="font-size: 16px;">{{ formatValue(Tags.data.top8[(4*(x-1)+n)-1].value[i]) }}</v-card-text>   
                      </div>
                  </v-col>
                  <v-col v-else>
                    <v-card-subtitle class="featuresTitle">{{ Tags.data.items[selectTags[(4*(x-1)+n)-1]].name }}</v-card-subtitle>
                     <!-- Loop to show the flag  -->
                      <div v-for="(flag, i) in Tags.data.flag" class="countryFlagIndicators">
                        <img align="left" class="countryFlag" :src="Tags.data.flag[i]" aspect-ratio="2" contain/>
                        <v-card-text style="font-size: 16px;">{{ formatValue(Tags.data.items[selectTags[(4*(x-1)+n)-1]].value[i]) }}</v-card-text>   
                      </div>  
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
            </v-row>

            <!--Next 8 features-->
            <v-row v-if="selectTags.length > 8" v-for="x in 2">
              <v-col v-for="n in 4" cols="3">
                <v-row>
                  <v-col v-if="selectTags.length > 4*(x+1)+n-1">
                    <v-card-subtitle class="featuresTitle">{{ Tags.data.items[selectTags[4*(x+1)+n-1]].name }}</v-card-subtitle>
                    <div v-for="(flag, i) in Tags.data.flag" class="countryFlagIndicators">
                      <img align="left" class="countryFlag" :src="Tags.data.flag[i]" aspect-ratio="2" contain/>
                      <v-card-text style="font-size: 16px;">{{ formatValue(Tags.data.items[selectTags[(4*(x-1)+n)-1]].value[i]) }}</v-card-text>   
                    </div>  
                  </v-col>
                  <v-divider vertical></v-divider>
                </v-row>
              </v-col>
            </v-row>

          </v-container>
        </v-card> 
        
        <v-alert
          dense
          outlined
          type="error"
          v-if="selectTags.length > 16"
        >
          You have reached the maximum number of features (16) to display
        </v-alert>
        
        <!--Max features selected notification-->

        <br/><br/>

        <!-- Chart -->
        <h2 class="sectionTitle">Key Financial Indicators</h2>
        <v-card class="mx-auto">
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
        <br/><br/>

        <h2 class="sectionTitle" v-if="countries.length == 1">Top 3 Similar Countries</h2>
        <v-card class="mx-auto">
          <v-container v-if="getTopThree === true">
            <v-row>
              <v-col v-for="n in 3" cols="3.5">
                <v-row>
                  <v-col>
                  <div class="top3Section">
                    <v-row class="mx-auto">
                      <img style="cursor: pointer" :src="topThree.data.items[n-1].flag" aspect-ratio="1.7" contain @click="() => topThreeOnClose(topThree.data.items[n-1].name)" contain/>
                      <v-card-subtitle class="top3CountryName">{{ topThree.data.items[n-1].name }}</v-card-subtitle>
                    </v-row>
                    <v-row class="mx-auto">
                      <div class="top3ScoreTitle">Score: {{ topThree.data.items[n-1].score.toFixed(4) }}</div>
                    </v-row>
                  </div>
                  </v-col>
                 <v-divider vertical></v-divider>
                </v-row>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>


      <country-region :dialog="dialog" :access="access" @close="onClose"/>
    </v-row>

  </v-container>
</template>

<script>
import CountryRegion from "@/components/home/CountryRegion";
import GoogleMap from "@/components/home/GoogleMap";
import lineChart from "@/components/analytics/lineChart";
import VueJsonToCsv from 'vue-json-to-csv'

export default {
  name: "GoogleBottomSheet",
  components: {CountryRegion, GoogleMap, VueJsonToCsv},
  props: {
    dialog: Boolean,
    access: String
  },
  data() {
    return {
      selectTags: [],
      Tags: null,
      chartdata: [],
      csvdata: [],
      isLoaded: false,
      isChartLoaded: false,
      getTopThree: false,
      getCsvData: false,
      data: null,
      topThree: null,
      countries: ['Singapore'],
      colors: ['black--text', 'blue--text', 'teal--text', 'blue-grey--text'],
    }
  },

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

        console.log("HUEHUEHUEHEUHE", response.data.items)

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
}
</script>

<style scoped>
  .sectionTitle {
    margin-bottom:10px;
  }

  .featuresTitle{
    color:#215085 !important;
    font-weight:700;
    font-size:16px;
    padding:16px;
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

  .charts {
    padding-left:10px;
    padding-right:10px;
  }

  .top3CountryName {
    color:#333333 !important;
    font-weight:700;
    font-size:16px;
  }

  .top3ScoreTitle {
    color:#215085 !important;
    font-weight:700;
    font-size:18px;
    margin-top:10px;
  }

  .top3Feature {
    color:#333333 !important;
    font-size:14px;
    margin-top:10px;
  }

  .top3Section {
    padding-left:10px;
    padding-right:10px;
    padding-bottom:10px;
  }

  .top3Indicators {
    color:#333333 !important;
    font-weight:700;
    font-size:16px;
    margin-top:15px;
  }

  .filtersSection {
    overflow-y: scroll;
    height:600px;
  }

  ::-webkit-scrollbar {
    -webkit-appearance: none;
    width: 6px;
  }

  ::-webkit-scrollbar-thumb {
    border-radius: 4px;
    background-color: rgba(0, 0, 0, .3);
    box-shadow: 0 0 1px rgba(255, 255, 255, .5);
  }

  .filtersSectionTag {
    color:#333333 !important;
    font-weight:700;
    font-size:16px;
    padding:0 16px 0 16px;
  }

  .v-btn.sidebar {
    min-width:200px;
    min-height:45px;
  }

  .sidebarCountryName{
    color:#333333 !important;
    font-weight:700;
    font-size:22px;
    text-align:center;
  }

  .countryFlag {
    height:32px;
    margin-top:10px;
    margin-left:16px;
  }

  .countryFlagIndicators {
    display: flex;
  }

  .countryFlagSidebar {
    height:48px;
    margin-bottom:10px;
  }

  .countryFlagSidebarSection {
    display: flex;
    justify-content: center;
    align-items: center;
    margin:0 auto;
  }

</style>