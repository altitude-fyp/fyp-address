<template>
    <div v-if="top10ChartData">    
        <v-row v-for="chart in top10ChartData":key=chart.title>
            <v-col>
                <!-- title for each chart goes here -->
                <div class="chartsTitle">
                    <h3>{{chart.title}}</h3>
                </div>

                <!-- each line-chart component goes here -->
                <div class="charts" v-if="chart">
                    <bar-chart :top10ChartData=chart>
                    </bar-chart>
                </div>
                <br>
                <p class="chartsDescription">{{chart.description}}</p>
            </v-col>
        </v-row>
    </div>
</template>

<script>

import BarChart from "@/components/analytics/barChart.vue"

export default {

    name: "npl-top10-chart",

    props: ["top10ChartData"],

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