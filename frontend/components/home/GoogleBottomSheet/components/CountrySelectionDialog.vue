<template>

    <div>
        <v-row justify="center">

            <v-dialog
                v-model="showCountrySelectionDialog"
                fullscreen
                hide-overlay
                transition="dialog-bottom-transition"
                scrollable>

                <v-card class="scroll">

                    <!-- toolbar: blue bar thing at the top of the dialog -->
                    <v-toolbar flat dark color="#004D8E" max-height="70px">
                        <!-- this is the cross button at the top left of the dialog -->
                        <!-- this button closes the dialog -->
                        <v-btn icon dark @click=closeCountrySelectionDialog>
                            <v-icon>mdi-close</v-icon>
                        </v-btn>

                        <!-- this here is the toolbar title -->
                        <v-toolbar-title>Select countries for comparison</v-toolbar-title>
                        <v-spacer></v-spacer>
                    </v-toolbar>

                    <!-- content of country selection dialog goes here -->
                    <v-row>
                        <div class="countrySearch">

                            <!-- title -->
                            <div class="countrySearchTitle">Select at least one country</div>

                            <!-- the cool autocomplete thing is here -->
                            <v-autocomplete
                                v-model="selectedCountries"
                                :items="allCountries"
                                chips multiple rounded filled clearable deletable-chips
                                :disable=disableCountrySearch>
                            </v-autocomplete>

                            <!-- error message for when user selects more than 4 countries -->
                            <v-card-subtitle
                                class="errorMessage"
                                v-if="disableCountrySearch">
                                You have selected the maximum number of countries for comparison, please select a maximum of 4 countries
                            </v-card-subtitle>

                            <!-- reset and submit button goes here -->
                            <div class="resetSubmitButtons">

                                <!-- reset button -->
                              <div style="padding-right:10px">
                                <v-btn class="button"
                                    depressed
                                    @click="resetSelectedCountries">
                                    Reset All
                                </v-btn>
                              </div>
                                <!-- submit button -->

                              <div v-if="selectedCountries.length <= 4">
                                <v-btn class="button white--text"
                                    depressed color="#004D8E"
                                    @click="submitSelectedCountries">
                                    Submit
                                </v-btn>
                              </div>
                              <div v-else>
                                <v-btn class="button white--text"
                                       depressed color="#004D8E"
                                       disabled
                                       @click="submitSelectedCountries">
                                  Submit
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

    name: "country-selection-dialog",

    props: ["showCountrySelectionDialog"],

    data() {
        return {
            allCountries: null,
            selectedCountries: []
        }
    },

    mounted() {
        this.getAllCountries()
    },

    methods: {

        closeCountrySelectionDialog() {
            // this function runs when the user clicks on the little cross button on the top left of the dialog
            // this function closes the dialog (or rather, tells its parent to close the dialog)
            this.$emit("closeCountrySelectionDialogEvent")
        },

        getAllCountries() {
            //this function gets all countries from backend in alphabetical order
            var url = process.env.BACKEND + "/api/countries/list"

            this.$axios.get(url).then((response) => {
                this.allCountries = response.data.countries
            })
        },

        resetSelectedCountries() {
            // this function is called when user clicks "reset" button
            this.selectedCountries = []
        },

        submitSelectedCountries() {
            //this function is called when user clicks "submit" button
            //this function passes selectedCountries to the parent component
            this.$emit("submitSelectedCountriesEvent", this.selectedCountries)
            this.closeCountrySelectionDialog()
        }

    },

    computed: {

        disableCountrySearch() {
            // this function returns a boolean: whether user has selected >= 4 countries
            return this.selectedCountries.length >= 4
        }
    }


}

</script>

<style>

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
