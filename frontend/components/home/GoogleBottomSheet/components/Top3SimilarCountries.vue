<template>

    <div v-if="top3similarCountries" style="padding-top: 50px;">

        <!-- title comes here -->
        <v-row>
            <h2 class="sectionTitle">Top 3 Similar Countries</h2>

            <v-tooltip bottom>
                <template v-slot:activator="{ on, attrs }">
                <v-icon
                    style="margin-left:10px;margin-bottom:10px"
                    color="#454545"
                    dark
                    v-bind="attrs"
                    v-on="on"
                >
                    mdi-information-outline
                </v-icon>
                </template>
                <span>The similarity score is calculated by comparing financial indicators such as</span><br/> 
                <span>Financial Development Index and Financial Institutions Index using cosine similarity.</span>
            </v-tooltip>
        </v-row>

        <v-card class="mx-auto">
            <v-container>

                <v-row>
                    <!-- Each country div goes here -->
                    <v-col v-for="country in top3similarCountries" cols="3.5" :key=country.name>

                        <v-row>
                            <v-col>

                                <!-- cards for top 3  -->
                                <div class="top3section">

                                    <v-row class="mx-auto">
                                        <!-- flag goes here -->
                                        <img :src="country.flag"
                                            style="cursor: pointer"
                                            aspect-ratio=1.7
                                            contain
                                            @click="selectCountry(country.name)"/>

                                        <!-- country name goes here -->
                                        <v-card-subtitle class="top3CountryName">
                                            {{ country.name }}
                                        </v-card-subtitle>
                                    </v-row>

                                    <v-row class="mx-auto">
                                        <!-- score goes here -->
                                        <div class="top3ScoreTitle">
                                            Score: {{ country.score.toFixed(4) }}
                                        </div>

                                    </v-row>

                                </div>

                            </v-col>
                        </v-row>



                    </v-col>
                </v-row>

            </v-container>
        </v-card>

    </div>

</template>

<script>

export default {

    name: "top-3-similar-countries",

    props: ["top3similarCountries"],

    methods: {

        selectCountry(countryName) {
            //this function is called when user clicks on any of the top 3 countries
            //passes this 1 country name to parent component to handle
            this.$emit("countrySelectedFromTop3Panel", [countryName])
        }

    }

}

</script>

<style>

.sectionTitle {
    margin-bottom:10px;
    padding-left: 15px;
}

.top3CountryName {
    color:#333333 !important;
    font-weight:700;
    font-size:16px;
}

.top3ScoreTitle {
    color:#215085 !important;
    font-weight:700;
    font-size:18px;
    margin-top:10px;
}

.top3Feature {
    color:#333333 !important;
    font-size:14px;
    margin-top:10px;
}

.top3Section {
    padding-left:10px;
    padding-right:10px;
    padding-bottom:10px;
}

.top3Indicators {
    color:#333333 !important;
    font-weight:700;
    font-size:16px;
    margin-top:15px;
}
</style>
