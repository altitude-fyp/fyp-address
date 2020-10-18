<template>

    <div v-if="selectedCountries && countriesMetadata && selectedFeatures && countryStatistics">

        <!-- title of component -->
        <h2 class="sectionTitle">Country Statistics</h2>

        <!-- this panel displays country features as selected by user -->
        <v-card class="mx-auto">
            <v-container>

                <!--Top 8 features-->
                <v-row v-for="i in 2" :key=i>
                    <v-col v-for="j in 4" cols="3" :key=j>

                        <v-row>
                            <v-col v-if="selectedFeatures[ j-1 + (i-1)*4 ]">
                                
                                <!-- title of feature goes here -->
                                <v-card-subtitle class="featuresTitle">
                                    {{ capitalize( selectedFeatures[ j-1 + (i-1)*4 ] ) }}
                                </v-card-subtitle>

                                <div v-for="cname in selectedCountries" :key=cname class="countryFlagIndicators">

                                    <!-- flag for each country goes here -->
                                    <img 
                                        :src="countriesMetadata[cname].flag"
                                        align="left"
                                        class="countryFlag"
                                        aspect-ratio="2"
                                        contain/>

                                    <!-- Value of feature for country goes here -->
                                    <v-card-text style="font-size: 16px;">
                                        {{formatValue(countryStatistics[cname][ selectedFeatures[ j-1 + (i-1)*4 ]])}}
                                    </v-card-text>

                                </div>

                            </v-col>

                            <!-- divider goes here - the vertical line between features -->
                            <v-divider vertical></v-divider>
                        </v-row>

                    </v-col>
                </v-row>   
                <!-- End of top 8 features -->

                <!-- Next 8 features-->
                <div v-if="selectedFeatures.length > 8">

                    <v-row v-for="i in 2" :key=i>
                        <v-col v-for="j in 4" cols="3" :key=j>

                            <v-row>
                                <v-col v-if="selectedFeatures[ j-1 + (i-1)*4 + 8]">
                                    
                                    <!-- title of feature goes here -->
                                    <v-card-subtitle class="featuresTitle">
                                        {{ capitalize( selectedFeatures[ j-1 + (i-1)*4 +8] ) }}
                                    </v-card-subtitle>

                                    <div v-for="cname in selectedCountries" :key=cname class="countryFlagIndicators">

                                        <!-- flag for each country goes here -->
                                        <img v-if="countriesMetadata[cname] && countriesMetadata[cname].flag"
                                            :src="countriesMetadata[cname].flag"
                                            align="left"
                                            class="countryFlag"
                                            aspect-ratio="2"
                                            contain/>

                                        <!-- Value of feature for country goes here -->
                                        <v-card-text style="font-size: 16px;">
                                            {{formatValue(countryStatistics[cname][ selectedFeatures[ j-1 + (i-1)*4 + 8]])}}
                                        </v-card-text>

                                    </div>

                                </v-col>

                                <!-- divider goes here - the vertical line between features -->
                                <v-divider vertical></v-divider>
                            </v-row>

                        </v-col>
                    </v-row>

                </div>
                <!-- End of next 8 features -->
        
        
            </v-container>
        </v-card>


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
    
.featuresTitle{
    color:#215085 !important;
    font-weight:700;
    font-size:16px;
    padding:16px;
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