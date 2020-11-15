<template>
  <v-container>
    <!--     HEADER -->
    <!--      Market Segmentation header -->
    <v-row>
      <v-col>
        <h2 style="color: #D9261C">
          <v-icon>mdi-filter
          </v-icon>
          Market Segmentation
        </h2>
      </v-col>
    </v-row>
    <!--      Filter in place box -->
    <v-row>
      <v-col>
        <v-card flat>
          <div v-if="panel.every(item => item === 0)">
            <v-card-title>
              No Filters Selected
            </v-card-title>
          </div>
          <div v-else>
            <v-card-title>
              The following filters are in place :
            </v-card-title>
            <v-card-subtitle>
              <!--              Filter in place for Economic Status-->
              <div v-if="panel[0] !== 0 && panel[0] !== 'None' ">
                Economic Status : {{ panel[0] }}
              </div>

              <div v-if="!content[1]['sliderDisable']">
                Household Monthly Income Work : {{ content[1]['ticksLabels'][panel[1]] }}
              </div>

              <div v-if="!content[2]['sliderDisable']">
                Income From Work : {{ content[2]['ticksLabels'][panel[2]] }}
              </div>

              <!--              Filter in place for Population Age Group-->
              <div v-if="panel[3] !== 0 && panel[0] !== 'None' ">
                Population Age Group : {{ panel[3] }}
              </div>
            </v-card-subtitle>
          </div>
          <!--      Reset All Filter Button -->
          <v-card-actions>
            <v-row justify="end">
              <v-btn
                outlined
                color="#D9261C"
                depressed
                small
                @click=resetAllFilters>
                Reset all filter
              </v-btn>
            </v-row>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>

    <!-- PANELS -->
    <div
      v-for="(item,i) in items"
      :key="i">

      <v-card-title><h4>{{ item }}</h4></v-card-title>

      <!-- Content of the expansion-->
      <v-card style="padding: 50px;">
        <!-- For Economic Status and Population Age Group it will be a single radio-->
        <div v-if="!content[i]['slider']">
          <v-radio-group
            v-model="panel[i]">

            <v-row justify="space-around">
              <!-- Population Age Group-->
              <div v-if="content[i]['ticksLabels'].length > 3" >
                <div v-for="j in content[i]['ticksLabels']" :key="j">
                  <v-col>
                    <v-radio
                      :key="j"
                      :label="j"
                      :value="j"
                    ></v-radio>
                  </v-col>
                </div>
              </div>
            </v-row>

            <!-- Economic status-->
            <div v-if="content[i]['ticksLabels'].length < 4" >
              <div v-for="j in content[i]['ticksLabels']" :key="j">
                <v-row style="padding: 5px;">
                  <v-radio
                    :key="j"
                    :label="j"
                    :value="j"
                  ></v-radio>
                </v-row>
              </div>
            </div>
          </v-radio-group>
        </div>


        <!-- For Income related, it will be a slider-->
        <div v-if="content[i]['slider']">
          <v-checkbox
            v-model="content[i]['sliderDisable']"
            :label="`Do not filter by ${item.toString()}`"
          ></v-checkbox>
          <v-slider
            v-model="panel[i]"
            :tick-labels="content[i]['ticksLabels']"
            :max="content[i]['max']"
            :disabled="content[i]['sliderDisable']"
            step="1"
            color="#D9261C"
            ticks="always"
            tick-size="6"
            thumb-size="24"
          ></v-slider>
        </div>

      </v-card>
    </div>

    <!--    Filter Data Submit Button-->
    <v-row>
      <v-col align="center"
             justify="center">
        <v-btn
          color="#D9261C"
          outlined
          class="mb-2"
          block
          large
          depressed
          @click="send2backend">
          Filter Data
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "marketSegmentation",
  data() {
    return {
      panel: [0, 0, 0, 0],
      items: ['Economic Status', 'Household Monthly Income Work', 'Income From Work', 'Population Age Group'],
      content: [
        {
          max: 1,
          slider: false,
          ticksLabels: [
            'None',
            'Unemployed',
            'Employed',
          ],
        },
        {
          max: 2,
          slider: true,
          sliderDisable: true,
          ticksLabels: [
            'Low [0-5000]',
            'Middle [5000-10000]',
            'High [10000+]',
          ]
        },
        {
          max: 2,
          slider: true,
          sliderDisable: true,
          ticksLabels: [
            'Low [0-3000]',
            'Middle [3000-6000]',
            'High [6000+]',
          ]
        },
        {
          max: 5,
          slider: false,
          ticksLabels: [
            'None',
            '20-30',
            '30-40',
            '40-50',
            '50-60',
            '60-70',
            '70-80'
          ]
        }],

    }
  },
  methods: {
    // Reset the panel

    send2backend() {

      let url = process.env.BACKEND + "/api/analytics/market_segment/"

      this.$axios.post(url, this.computedPanel).then(response => {
        if (response.data.status == "success") this.$emit("filteredRegionsDataReceived", response.data.regions)
      })
      
      this.resetAllFilters()
    },

    resetAllFilters() {
      // panel will hold the values to be sent to backend and retrieved
      // Example of sending format : this.panel = [ "Employed", 1, 2, "40-50" ]
      this.panel = [0, 0, 0, 0]
    },
  },

  computed: {

    computedPanel() {

      let hhi = ["Low [0-5000]", "Middle [5000-10000]", "High [10000+]"][this.panel[1]]
      let i = ["Low [0-3000]", "Middle [3000-6000]", "High [6000+]"][this.panel[2]]

      if (this.content[1].sliderDisable) hhi = ""
      if (this.content[2].sliderDisable) i = ""

      let econ = this.panel[0]
      if (econ == 0) econ=""

      let pag = this.panel[3]
      if (pag == 0) pag=""

      return {
        economic_status: econ,
        household_monthly_income_work : hhi,
        income_from_work : i,
        population_age_group: pag,

      }
    }

  }
}

</script>

<style scoped>

</style>
