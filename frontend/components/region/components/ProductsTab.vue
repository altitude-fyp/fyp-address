<template>

    <div v-if="productsChartData">

        <v-card flat class="mx-auto">
            <v-container style="text-align:center">

                <!-- Recommended Financial Products -->
                <h4 class="tabSubtitle">Recommended Financial Products</h4>
                <v-row align="center" justify="center">
                    <v-col>
                    <div v-for="(region,i) in productsChartData.products" :key=i>
                        <div class="productRegionName">
                            {{ region.region }}
                        </div>

                        <div v-for="(regionProducts,j) in region.products" :key=j>
                            <span style="margin-left:20px; margin-right:20px;" v-for="(regionProduct,k) in regionProducts" :key=k>
                                {{ regionProduct }}
                            </span>
                        </div><br/><br/>
                    </div>
                    </v-col>
                </v-row>
            
                <v-divider></v-divider>

                <br/>
            
                <v-row>
                    <!-- 1st Graph -->
                    <v-col>
                        <!-- Title of 1st Graph -->
                        <div class="chartsTitle">
                            <h3>{{productsChartData.graph_1.title}}</h3><br/>
                        </div>
                            <indifference-line-chart :productsChartData=productsChartData></indifference-line-chart>
                             <p class="chartsDescription">{{productsChartData.graph_1.description}}</p>
                        <br/>
                    </v-col>

                    <!-- 2nd Graph -->
                    <v-col>
                        <!-- Title of 2nd Graph -->
                        <div class="chartsTitle">
                            <h3>{{productsChartData.graph_2.title}}</h3>
                        </div>

                        <div class="charts">
                            <utility-line-chart :productsChartData=productsChartData></utility-line-chart>
                            <p class="chartsDescription">{{productsChartData.graph_2.description}}</p>
                        </div>   
                    </v-col>
                </v-row>

            </v-container>
        </v-card>

    </div>

</template>

<script>

import IndifferenceLineChart from "@/components/region/components/ProductsIndifferenceChart.vue"
import UtilityLineChart from "@/components/region/components/ProductsUtilityChart.vue"

export default {

    name: "region-products-tab",

    props: ["productsChartData"],

    components: {
        "indifference-line-chart": IndifferenceLineChart,
        "utility-line-chart": UtilityLineChart
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
    margin-top:20px;
}

.charts {
    padding-left:10px;
    padding-right:10px;
}

.productRegionName {
    font-size:20px;
    font-weight:700;
    text-transform:capitalize;
    color:#215085;
    margin-bottom:10px;
}

.recommendedProductList {
    list-style-image: url('https://i.imgur.com/4TrN1dY.png');
}

.tabSubtitle {
    margin-top:15px;
    margin-bottom:10px;
}

</style>