<template>

    <div v-if="productsChartData">

        <v-card flat class="mx-auto">
            <v-container>
                <h4>Recommended Financial Products</h4>
                <v-row>
                    <div v-for="region in productsChartData.products" :key="region.region">
                        <v-col style="margin-right:50px">
                            <div class="productRegionName">
                                {{ region.region }}
                            </div>

                            <ul v-for="regionProducts in region.products" :key=regionProducts class="recommendedProductList">
                                <li v-for="regionProduct in regionProducts" :key=regionProduct>

                                    {{ regionProduct }}
                                   
                                </li>
                            </ul>
                        </v-col>
                    </div>
                </v-row>

                <br/>

                <v-divider></v-divider>

                <br/>
            
                <v-row>
                    <!-- 1st Graph -->
                    <v-col>
                        <!-- Title of 1st Graph -->
                        <div class="chartsTitle">
                            <h3>{{productsChartData.graph_1.title}}</h3>
                        </div>

                        <div class="charts">
                            
                        </div>
                    </v-col>

                    <!-- 2nd Graph -->
                    <v-col>
                        <!-- Title of 2nd Graph -->
                        <div class="chartsTitle">
                            <h3>{{productsChartData.graph_2.title}}</h3>
                        </div>

                        <div class="charts">
                            
                        </div>   
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

</style>