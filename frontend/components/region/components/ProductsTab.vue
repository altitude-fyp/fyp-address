<template>

    <div v-if="productsChartData">

        <!-- title goes here -->
        <!-- <h2 class="sectionTitle">Key Financial Indicators</h2> -->

        <v-card class="mx-auto">
            <v-container>
            
                <v-row>
                     <v-col>
                        <v-row>
                            <v-col>
                                <!-- title for each chart goes here -->
                                <div class="chartsTitle">
                                    <h3>{{productsChartData.graph_1.title}}</h3>
                                </div>

                                <!-- each line-chart component goes here -->
                                <div class="charts">
                                    <line-chart :productsChartData=productsChartData>
                                    </line-chart>
                                </div>
                                <br>
                            </v-col>
                        </v-row>
                    </v-col>
                </v-row>

            </v-container>
        </v-card>

    </div>

</template>

<script>

import LineChart from "@/components/region/components/ProductsLineChart.vue"

export default {

    name: "region-products-tab",

    props: ["productsChartData"],

    components: {
        "line-chart": LineChart
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