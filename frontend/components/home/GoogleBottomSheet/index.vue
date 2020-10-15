<template>
    <v-container>
        
        <v-row>
            
            <v-col cols=3>

                <metadata-panel 
                    :selectedCountries=selectedCountries
                    :countriesMetadata=countriesMetadata
                    @selectCountriesButtonClicked=openCountrySelectionDialog>
                </metadata-panel>
                
                <v-divider></v-divider>

                <feature-selection-panel 
                    :selectableFeatures=selectableFeatures 
                    @checkboxChange=updateSelectedFeatures>
                </feature-selection-panel>

            </v-col>

            <v-col cols="9">

                <country-statistics
                    :countriesMetadata=countriesMetadata
                    :countryStatistics=countryStatistics
                    :selectedCountries=selectedCountries
                    :selectedFeatures=selectedFeatures>
                </country-statistics>

                <key-financial-indicators></key-financial-indicators>

                <top-3></top-3>

                {{selectedCountries}}
                {{countriesMetadata}}

            </v-col>

        </v-row>

        <country-selection-dialog 
            :showCountrySelectionDialog=showCountrySelectionDialog
            @closeCountrySelectionDialogEvent="closeCountrySelectionDialog"
            @submitSelectedCountriesEvent="updateSelectedCountries">
        </country-selection-dialog>

    </v-container>
</template>

<script>

import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel.vue"
import CountrySelectionDialog from "@/components/home/GoogleBottomSheet/components/CountrySelectionDialog.vue"
import FeatureSelectionPanel from "@/components/home/GoogleBottomSheet/components/FeatureSelectionPanel.vue"
import CountryStatistics from "@/components/home/GoogleBottomSheet/components/CountryStatistics.vue"
import KeyFinancialIndicators from "@/components/home/GoogleBottomSheet/components/KeyFinancialIndicators.vue"
import Top3 from "@/components/home/GoogleBottomSheet/components/Top3.vue"


export default {
    
    components: {
        "metadata-panel": MetadataPanel,
        "country-selection-dialog": CountrySelectionDialog,
        "feature-selection-panel": FeatureSelectionPanel,
        "country-statistics": CountryStatistics,
        "key-financial-indicators": KeyFinancialIndicators,
        "top-3": Top3,
    },

    props: [],

    data() {
        return {
            selectedCountries: ["Singapore"],
            countriesMetadata: null,
            selectableFeatures: null,
            selectedFeatures: [
                "gdp nominal",
                "unemployment rate",
                "Financial Development Index",
                "population density",
                "literacy rate",
                "life expectacy (overall)",
                "gini",
                "Consumer Price Index, All items",
            ],
            countryStatistics: null,
            showCountrySelectionDialog: false,
        }
    },

    mounted() {
        this.getEverything()
    },

    methods: {

        getEverything() {
            //this function renders everything based on this.selectedCountries
            this.getCountriesMetadata()
            this.getSelectableFeatures()
            this.getCountryStatistics()
        },
    
        getCountriesMetadata() {
            // get flag, lat, lon, country code of each country in countries
            this.countriesMetadata = null
            var url = process.env.BACKEND + "/api/countries/metadata/" + this.selectedCountries

            this.$axios.get(url).then((response) => {
                this.countriesMetadata = response.data
            })
        },

        openCountrySelectionDialog() {
            // this function is called when the user clicks on "countries to compare"
            //this function opens the country selection dialog
            this.showCountrySelectionDialog = true
        },

        closeCountrySelectionDialog() {
            //this function closes the country selection dialog
            this.showCountrySelectionDialog = false
        },

        updateSelectedCountries(selectedCountries) {
            //this function is called after user submits his selected countries from the country selection dialog
            this.selectedCountries = selectedCountries
            this.getEverything()
        },

        getSelectableFeatures() {
            // get all selectable features classified by category
            this.selectableFeatures = null
            var url = process.env.BACKEND + "/api/countries/selectableFeatures/"

            this.$axios.get(url).then((response) => {
                this.selectableFeatures = response.data
            })
        },

        updateSelectedFeatures(features) {
            // this function triggers on change on checkboxes in selected features
            this.selectedFeatures = features
        },


        getCountryStatistics() {
            // get statistics from aggregate.countries
            this.countryStatistics = null
            var url = process.env.BACKEND + "/api/countries/statistics/" + this.selectedCountries

            this.$axios.get(url).then((response) => {
                this.countryStatistics = response.data
            })

        }
    }


}

</script>