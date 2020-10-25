<template>

    <div v-if="selectedCountries && countriesMetadata && selectedFeatures && countryStatistics">
        <!--Top 8 features-->
        <v-row v-for="i in 2" :key=i>
            <v-col v-for="j in 4" :key=j>
                
                <!-- title of feature goes here -->
                <v-card-subtitle class="featuresTitle">
                    {{ capitalize( selectedFeatures[ j-1 + (i-1)*4 ] ) }}
                </v-card-subtitle>

                <div v-for="cname in selectedCountries" :key=cname class="countryFlagIndicators">
                    <!-- Value of feature for country goes here -->
                    <v-card-text class="featuresSubTitle">
                        {{formatValue(countryStatistics[cname][ selectedFeatures[ j-1 + (i-1)*4 ]])}}
                    </v-card-text>
                </div>
                
            </v-col>
        </v-row>   
        <!-- End of top 8 features -->
    </div>

</template>

<script>

export default {

    name: "country-statistics",

    props: ["countriesMetadata", "countryStatistics", "selectedCountries", "selectedFeatures"],

    methods: {

        capitalize(string) {
            return string.slice(0,1).toUpperCase() + string.slice(1)
        },

        formatValue(num) {
            return Math.abs(Number(num)) >= 1.0e+9

            ? (Math.abs(Number(num)) / 1.0e+9).toFixed(2) + " billion"

            : Math.abs(Number(num)) >= 1.0e+6

            ? (Math.abs(Number(num)) / 1.0e+6).toFixed(2) + " million"

            : +(Math.round(num + "e+4")  + "e-4");
        },

    }

}

</script>

<style>
    
.featuresTitle {
    color:#215085 !important;
    font-weight:700;
    font-size:14px !important;
    padding:16px;
    text-align:center;
}

.featuresSubTitle {
    font-size:14px !important;
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

</style>