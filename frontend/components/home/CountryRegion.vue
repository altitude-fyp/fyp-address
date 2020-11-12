<template>
  <div>
    <v-row
      justify="center"
    >

      <v-dialog
        v-model="dialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable
      >
        <v-card
          class="scroll"
        >
          <v-toolbar
            flat
            dark
            color="#004D8E"
            max-height="70px"
          >
            <v-btn
              icon
              dark
              @click="$emit('close', ['close'])">
              <v-icon>mdi-close</v-icon>
            </v-btn>
            <v-toolbar-title>Select {{ access }} for Comparison</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>

          <!-- REGION SELECT -->
          <v-row v-if="region && access==='Regions' ">
            <div class="countrySearch">
              <div class="countrySearchTitle">Select at least one region</div>
              <v-autocomplete
                v-model="regionSelect"
                :items="region.data.items"
                chips
                multiple
                rounded
                filled
                clearable
                deletable-chips
              ></v-autocomplete>

              <v-card-subtitle class="errorMessage" v-if="regionSelect.length === 4">You have selected the maximum
                number
                of regions for
                comparison
              </v-card-subtitle>

              <div class="resetSubmitButtons">
                <v-btn class="button" depressed @click="regionSelect=[]">Reset All</v-btn>
                <div v-if="regionSelect.length === 0">
                  <v-btn class="button white--text" depressed color="#004D8E" @click="$emit('close',['close'])">Submit
                  </v-btn>
                </div>
                <div v-else>
                  <v-btn class="button white--text" depressed color="#004D8E"
                         @click="$emit('close',['country', regionSelect])">Submit
                  </v-btn>
                </div>
              </div>
            </div>

          </v-row>


          <!-- COUNTRY SELECT -->
          <v-row v-if="country && access==='Countries' ">
            <div class="countrySearch">
              <div class="countrySearchTitle">Select at least one country</div>
              <v-autocomplete
                v-model="countrySelect"
                :items="country.data.items"
                chips
                multiple
                rounded
                filled
                clearable
                deletable-chips
              ></v-autocomplete>

              <v-card-subtitle class="errorMessage" v-if="countrySelect.length > 4">You have selected the maximum
                number of countries for
                comparison, please only select 4 countries
              </v-card-subtitle>

              <div class="resetSubmitButtons">
                <v-btn class="button" depressed @click="countrySelect=[]">Reset All</v-btn>
                <div v-if="countrySelect.length === 0">
                  <v-btn class="button white--text" depressed color="#004D8E" @click="$emit('close',['close'])">Submit
                  </v-btn>
                </div>
                <div v-else>
                  <v-btn v-if="countrySelect.length > 4" class="button white--text" disabled>
                    Submit
                  </v-btn>
                  <v-btn v-else class="button white--text" depressed color="#004D8E"
                         @click="$emit('close',['country', countrySelect])">Submit
                  </v-btn>

                </div>
              </div>
            </div>

          </v-row>

        </v-card>

      </v-dialog>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "CountryRegion",
  props: {
    dialog: Boolean,
    access: String,
    countries: Array,
    regions: Array,
  },
  data() {
    return {
      countrySelect: [],
      countryRegion: '',
      n: 0,
      regionSelect: [],
      country: null,
      region: null,
      disable: false,
    }
  },
  mounted() {
    this.$axios.$get(process.env.BACKEND + `/api/countries`)
      .then((country) => {
        this.country = country // Put inside an object
        console.log(country)
      })
    this.$axios.$get(process.env.BACKEND + `/api/regions/list`)
      .then((region) => {
        this.region = region // Put inside an object
      }).error(e => {console.log(e)})
  },

  methods: {
    resetDialog() {
      this.$emit('resetDialog', false)
    },
  },
}
</script>
<style scoped>
.scroll {
  overflow-y: scroll
}

.continentTitle {
  text-align: center;
}

.bottomBar {
  position: fixed;
  left: 0;
  bottom: 0;
  width: 100%;
  background-color: white;
  text-align: center;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
}

.v-btn.button {
  margin: 25px 10px 0 10px;
}

.resetSubmitButtons {
  display: flex;
  justify-content: center;
  align-items: center;
}

.errorMessage {
  color: #d33232 !important;
  text-align: center;
}

.selectedCountry {
  color: #215085 !important;
  margin: 0 20px 0 20px;
  font-size: 20px;
  font-weight: 700;
}

.countrySearch {
  width: 700px;
  margin: 0 auto;
}

.countrySearchTitle {
  color: #333333;
  font-weight: 700;
  font-size: 20px;
  text-align: center;
  margin-top: 150px;
  margin-bottom: 15px;
}
</style>

