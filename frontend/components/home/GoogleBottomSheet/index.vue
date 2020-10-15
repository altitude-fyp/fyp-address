<template>
    <v-container>
        
        <v-row>
            
            <v-col cols=3>

                <metadata-panel 
                    :selectedCountries=selectedCountries
                    :countriesMetadata=countriesMetadata>
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

            </v-col>

        </v-row>

    </v-container>
</template>

<script>

import MetadataPanel from "@/components/home/GoogleBottomSheet/components/MetadataPanel.vue"
import FeatureSelectionPanel from "@/components/home/GoogleBottomSheet/components/FeatureSelectionPanel.vue"
import CountryStatistics from "@/components/home/GoogleBottomSheet/components/CountryStatistics.vue"
import KeyFinancialIndicators from "@/components/home/GoogleBottomSheet/components/KeyFinancialIndicators.vue"
import Top3 from "@/components/home/GoogleBottomSheet/components/Top3.vue"

export default {
    
    components: {
        "metadata-panel": MetadataPanel,
        "feature-selection-panel": FeatureSelectionPanel,
        "country-statistics": CountryStatistics,
        "key-financial-indicators": KeyFinancialIndicators,
        "top-3": Top3
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
            countryStatistics: null
        }
    },

    mounted() {
        this.getCountriesMetadata()
        this.getSelectableFeatures()
        this.getCountryStatistics()
    },

    methods: {
    
        getCountriesMetadata() {
            // get flag, lat, lon, country code of each country in countries
            var url = process.env.BACKEND + "/api/countries/metadata/" + this.selectedCountries

            this.$axios.get(url).then((response) => {
                this.countriesMetadata = response.data
            })
        },

        getSelectableFeatures() {
            // get all selectable features classified by category
            var url = process.env.BACKEND + "/api/countries/selectableFeatures/" + this.selectedCountries

            this.$axios.get(url).then((response) => {
                this.selectableFeatures = response.data
            })
        },

        updateSelectedFeatures(data) {
            // this function triggers on change on checkboxes in selected features
            // this function updates selectedFeatures
            this.selectedFeatures = data
        },


        getCountryStatistics() {
            // get statistics from aggregate.countries
            var url = process.env.BACKEND + "/api/countries/statistics/" + this.selectedCountries

            this.$axios.get(url).then((response) => {
                this.countryStatistics = response.data
            })

        }
    }


}

</script>