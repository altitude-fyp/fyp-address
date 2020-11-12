<template>
  <div>
    <v-row justify="center">

      <v-dialog
        v-model="showRegionSelectionDialog"
        fullscreen
        hide-overlay
        transition="dialog-bottom-transition"
        scrollable>

        <v-card class="scroll">

          <!-- toolbar: blue bar thing at the top of the dialog -->
          <v-toolbar flat dark color="#004D8E" max-height="70px">
            <!-- this is the cross button at the top left of the dialog -->
            <!-- this button closes the dialog -->
            <v-btn icon dark @click=closeRegionSelectionDialog>
              <v-icon>mdi-close</v-icon>
            </v-btn>

            <!-- this here is the toolbar title -->
            <v-toolbar-title>Select regions for comparison</v-toolbar-title>
            <v-spacer></v-spacer>
          </v-toolbar>

          <!-- content of country selection dialog goes here -->
          <v-row>
            <div class="regionSearch">

              <!-- title -->
              <div class="regionSearchTitle">Select at least one region</div>

              <!-- the cool autocomplete thing is here -->
              <v-autocomplete
                v-model="selectedRegions"
                :items="allRegions"
                chips multiple rounded filled clearable deletable-chips
                :disable=disableRegionSearch>
              </v-autocomplete>

              <!-- error message for when user selects more than 4 countries -->
              <v-card-subtitle
                class="errorMessage"
                v-if="disableRegionSearch">
                You have selected the maximum number of regions for comparison, please select a maximum of 4 regions
              </v-card-subtitle>

              <!-- reset and submit button goes here -->
              <div class="resetSubmitButtons">

                <!-- reset button -->
                <div style="padding-right:10px">
                  <v-btn class="button"
                         depressed
                         @click="resetSelectedRegions">
                    Reset All
                  </v-btn>
                </div>
                <!-- submit button -->

                <div v-if="selectedRegions.length <= 4">
                  <v-btn class="button white--text"
                         depressed color="#004D8E"
                         @click="submitSelectedRegions">
                    Submit
                  </v-btn>
                </div>
                <div v-else-if="selectedRegions.length > 4">
                  <v-btn class="button white--text"
                         depressed color="#004D8E"
                         disabled
                         @click="submitSelectedRegions">
                    Submit
                  </v-btn>
                </div>

                <!--IF REGIONS SELECTED == 0 REDIRECTED TO HOMEPAGE-->

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
  name: "RegionSelectionDialog",
  props: ["showRegionSelectionDialog"],

  data() {
    return {
      allRegions: null,
      selectedRegions: []
    }
  },
  mounted() {
    this.getAllRegions()
  },

  methods: {

    closeRegionSelectionDialog() {
      // this function runs when the user clicks on the little cross button on the top left of the dialog
      // this function closes the dialog (or rather, tells its parent to close the dialog)
      this.$emit("closeRegionSelectionDialogEvent")
    },

    resetSelectedRegions() {
      // this function is called when user clicks "reset" button
      this.selectedRegions = []
    },

    submitSelectedRegions() {
      //this function is called when user clicks "submit" button
      //this function passes selectedCountries to the parent component
      this.$emit("submitSelectedRegionsEvent", this.selectedRegions)
      this.closeRegionSelectionDialog()
    },
    getAllRegions() {
      //this function gets all countries from backend in alphabetical order
      var url = process.env.BACKEND + "/api/regions/list"
      this.$axios.get(url).then((response) => {
        this.allRegions = response.data.data
      })
    },

  },

  computed: {

    disableRegionSearch() {
      // this function returns a boolean: whether user has selected >= 4 countries
      return this.selectedRegions.length >= 4
    }
  }
}
</script>

<style scoped>

.regionSearch {
  width:700px;
  margin: 0 auto;
}

.regionSearchTitle {
  color:#333333;
  font-weight:700;
  font-size:20px;
  text-align:center;
  margin-top:150px;
  margin-bottom:15px;
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

</style>

