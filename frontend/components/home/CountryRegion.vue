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

          <v-card
            class="mx-auto"
            max-width="900"
            outlined
            style="margin-top: 30px;"
            v-if='access==="Region"'
          >
            <v-card-subtitle selected the following regions for comparison:</v-card-subtitle>
            <v-card-subtitle>{{ regionSelect }}</v-card-subtitle>

            <div style="padding:10px;">
              <v-btn class="button" depressed @click="regionSelect=[]">Reset All</v-btn>
              
                <div v-if="regionSelect.length === 0">
                  <v-btn class="white--text" depressed color="#004D8E" @click="$emit('close',['close'])">Submit</v-btn>
                </div>
                <div v-else>
                  <v-btn class="white--text" depressed color="#004D8E" @click="$emit('close',['region', regionSelect])">Submit</v-btn>
                </div>


            </div> <!--Region Select Button-->

          </v-card>
           <!--Region Data-->
          <!-- <v-row v-if="region && access==='Region' ">
            <v-col v-for="reg in region.data">
              <v-list
                dense
              >
                <v-list-item style="padding-top: 20px">
                  <v-list-item-content>

                    <h1>{{ reg }}</h1>

                  <ul>
                    <v-checkbox v-model="countrySelect" v-for='dist in reg.countries' :label='dist'
                                :value='dist'>
                    </v-checkbox>
                  </ul>

                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-col>
          </v-row>  -->
          <!--WAIT FOR UPDATED REGION-->

          <!-- XAVIER you start from here -->
          <v-row v-if="country && access==='Countries' ">
          <div class="countrySearch">
            <div class="countrySearchTitle">Select at least one country</div>
            <v-autocomplete
              v-model="countrySelect"
              :items="country.data.items"
              :item-disabled="countrySelect.length >= 4"
              chips
              multiple
              rounded
              filled
              clearable
              deletable-chips
            ></v-autocomplete>

            <v-card-subtitle class="errorMessage" v-if="countrySelect.length === 4">You have selected the maximum number of countries for
              comparison
            </v-card-subtitle>

            <div class="resetSubmitButtons">
              <v-btn class="button" depressed @click="countrySelect=[]">Reset All</v-btn>
                <div v-if="countrySelect.length === 0">
                  <v-btn class="button white--text" depressed color="#004D8E" @click="$emit('close',['close'])">Submit</v-btn>
                </div>
                <div v-else>
                  <v-btn class="button white--text" depressed color="#004D8E" @click="$emit('close',['country', countrySelect])">Submit</v-btn>
                </div>
            </div>
          </div>
            <!-- <v-col v-for="item in country.data.items">
              <v-list
                dense
              >
                <v-list-item style="padding-top: 20px">
                  <v-list-item-content>

                    <h2 class="continentTitle">{{ reg.header }}</h2>

                    <ul>
                      <v-checkbox v-model="countrySelect" v-for='dist in country.data.items' :label='dist'
                                  :value='dist' :disabled="countrySelect.length >= 4">
                      </v-checkbox>
                    </ul>
                    
                  </v-list-item-content>
                </v-list-item>
              </v-list>
          </v-col>-->
          </v-row>

        <!--
        <div class="bottomBar">
          <v-card
            class="mx-auto elevation-0"
            max-width="900"
            v-if='access==="Countries"'
          >
            <br/>
            <v-card-subtitle>You have selected the following countries for comparison:</v-card-subtitle>
            
              <span class="selectedCountry" v-for="selected in countrySelect">{{selected}}</span>

            <v-card-subtitle class="errorMessage" v-if="countrySelect.length === 4">You have selected the maximum number of countries for
              comparison
            </v-card-subtitle>

            <div class="resetSubmitButtons">
              <v-btn class="button" depressed @click="countrySelect=[]">Reset All</v-btn>
                <div v-if="countrySelect.length === 0">
                  <v-btn class="button white--text" depressed color="#004D8E" @click="$emit('close',['close'])">Submit</v-btn>
                </div>
                <div v-else>
                  <v-btn class="button white--text" depressed color="#004D8E" @click="$emit('close',['country', countrySelect])">Submit</v-btn>
                </div>
            </div>

          </v-card>
        </div>-->
        </v-card>

      </v-dialog>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "CountryRegion",
  props: {
    dialog: {
      type: Boolean,
    },
    access: {
      type: String,
    },
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
    this.$axios.$get( process.env.BACKEND + `/api/countries`)
      .then((country) => {
        this.country = country // Put inside an object
      })
    this.$axios.$get(process.env.BACKEND + `/api/regions`)
      .then((region) => {
        this.region = region // Put inside an object
      })
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
    text-align:center;
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
    margin:25px 10px 0 10px;
  }

  .resetSubmitButtons {
    display: flex;
    justify-content: center;
    align-items: center;
  }

  .errorMessage {
    color:#d33232 !important;
    text-align:center;
  }

  .selectedCountry {
    color:#215085 !important;
    margin:0 20px 0 20px;
    font-size:20px;
    font-weight:700;
  }

  .countrySearch {
    width:700px;
    margin: 0 auto;
  }

  .countrySearchTitle {
    color:#333333;
    font-weight:700;
    font-size:20px;
    text-align:center;
    margin-top:150px;
    margin-bottom:15px;
  }
</style>