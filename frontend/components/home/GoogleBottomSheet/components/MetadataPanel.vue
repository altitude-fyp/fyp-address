<template>

    <div>

        <v-card class="mx-auto" outlined v-if="selectedCountries && countriesMetadata">

            <!-- for loop: displays country name and flag image -->
            <div v-for="cname in selectedCountries" :key=cname>
                
                <v-row class="mx-auto">
                    <v-col class="mx-auto">
                        <div class="sidebarCountryName">{{ cname }}</div>
                    </v-col>
                </v-row>

                <v-row>
                    <div class="countryFlagSidebarSection">
                        <img class="countryFlagSidebar" :src="countriesMetadata[cname].flag" aspect-ratio="2" contain/>
                    </div>
                </v-row>

            </div> 

            <!-- Countries to compare button -->
            <v-row justify="center">
                
                <v-btn
                    color="#004D8E"
                    class="white--text mb-2 sidebar"
                    depressed> 
                    
                    Countries to Compare
                </v-btn>

            </v-row>

            <!-- download csv button -->
            <!-- <v-row justify="center">
                
                <vue-json-to-csv :json-data="csvdata" :csv-title="'countries_data'">
                
                    <v-btn
                        outlined
                        color="#004D8E"
                        class="mb-2 sidebar"
                        depressed>
                        
                        <v-icon style="margin-right:5px">
                            mdi-download
                        </v-icon>
                            
                        Download CSV
                    </v-btn>
                    
              </vue-json-to-csv>

            </v-row> -->

        </v-card>

    </div>


</template>

<script>

export default {

    name: "metadata-panel",

    props: ["selectedCountries", "countriesMetadata"],

}

</script>

<style>
    
.sidebarCountryName{
    color:#333333 !important;
    font-weight:700;
    font-size:22px;
    text-align:center;
}

.countryFlagSidebar {
    height:48px;
    margin-bottom:10px;
}

.countryFlagSidebarSection {
    display: flex;
    justify-content: center;
    align-items: center;
    margin:0 auto;
}



</style>