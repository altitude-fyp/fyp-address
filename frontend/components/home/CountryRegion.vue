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
            color="primary"
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
            <v-card-subtitle>You have selected the following regions for comparison:</v-card-subtitle>
            <v-card-subtitle>{{ regionSelect }}</v-card-subtitle>

            <div style="padding:10px;">
              <v-btn depressed @click="regionSelect=[]">Reset All</v-btn>
              <div style="float:right">
                <div v-if="regionSelect.length === 0">
                  <v-btn depressed color="primary" @click="$emit('close',['close'])">Submit</v-btn>
                </div>
                <div v-else>
                  <v-btn depressed color="primary" @click="$emit('close',['region', regionSelect])">Submit</v-btn>
                </div>
              </div>

            </div> <!--Region Select Button-->

          </v-card> <!--Region Data-->
          <v-row v-if="region && access==='Region' ">
            <v-col v-for="reg in region.data">
              <v-list
                dense
              >
                <v-list-item style="padding-top: 80px">
                  <v-list-item-content>

                    <h1>{{ reg }}</h1>

                    <!--                    <ul>
                                          <v-checkbox v-model="countrySelect" v-for='dist in reg.countries' :label='dist'
                                                      :value='dist'>
                                          </v-checkbox>
                                        </ul>-->

                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-col>
          </v-row> <!--WAIT FOR UPDATED REGION-->


          <v-card
            class="mx-auto"
            max-width="900"
            outlined
            style="margin-top: 30px;"
            v-if='access==="Countries"'
          >
            <v-card-subtitle>You have selected the following countries for comparison:</v-card-subtitle>
            <v-card-subtitle>{{ countrySelect }}</v-card-subtitle>
            <v-card-subtitle v-if="countrySelect.length === 4">You have selected the maximum number of countries for
              comparison
            </v-card-subtitle>

            <div style="padding:10px;">
              <v-btn depressed @click="countrySelect=[]">Reset All</v-btn>
              <div style="float:right">
                <div v-if="countrySelect.length === 0">
                  <v-btn depressed color="primary" @click="$emit('close',['close'])">Submit</v-btn>
                </div>
                <div v-else>
                  <v-btn depressed color="primary" @click="$emit('close',['country', countrySelect])">Submit</v-btn>
                </div>
              </div>
            </div> <!--Button for country-->

          </v-card><!--Country Data-->
          <v-row v-if="country && access==='Countries' ">
            <v-col v-for="reg in country.data.items">
              <v-list
                dense
              >
                <v-list-item style="padding-top: 80px">
                  <v-list-item-content>

                    <h1>{{ reg.header }}</h1>

                    <ul>
                      <v-checkbox v-model="countrySelect" v-for='dist in reg.countries' :label='dist'
                                  :value='dist' :disabled="countrySelect.length >= 4">
                      </v-checkbox>
                    </ul>

                  </v-list-item-content>
                </v-list-item>
              </v-list>
            </v-col>
          </v-row> <!--Listing the countries based on DB-->


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
    this.$axios.$get(`http://lzl.blue/api/countries`)
      .then((country) => {
        this.country = country // Put inside an object
      })
    this.$axios.$get(`http://lzl.blue/api/regions`)
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
</style>

