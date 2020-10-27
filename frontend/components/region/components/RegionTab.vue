<template>

    <div v-if="chartData">

        <!-- title goes here -->
        <!-- <h2 class="sectionTitle">Key Financial Indicators</h2> -->

        <v-card class="mx-auto">
            <v-container>
            
                <v-row>
                    <v-col v-for="chart in chartData" cols=6 :key=chart.title>

                        <v-row>
                            
                            <v-col>
                                <!-- title for each chart goes here -->
                                <div class="chartsTitle">
                                    <h3>{{chart.title}}</h3>
                                </div>

                                <!-- each line-chart component goes here -->
                                <div class="charts" v-if="chart">

                                    <bar-chart :chartData=chart></bar-chart>

                                </div>
                                <br>
                                <!-- <p class="chartsDescription">{{chart.description}}</p> -->

                            </v-col>

                        </v-row>
                    
                    </v-col>
                </v-row>

            </v-container>
        </v-card>

    </div>

</template>

<script>

import BarChart from "@/components/region/components/RegionBarChart.vue"

export default {

    name: "region-tab",

    props: ["chartData"],

    components: {
        "bar-chart": BarChart
    },

    data() {
        return {}
    },

}

</script>

<style>
    
.chartsTitle{
    color:#d29a42;
    margin-bottom:10px;
    text-align:center;
}

.chartsDescription {
    font-size:13px;
    padding-left:10px;
    padding-right:10px;
}

.charts {
    padding-left:10px;
    padding-right:10px;
}

</style>