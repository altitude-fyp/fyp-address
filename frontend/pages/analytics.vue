<template>
  <v-app>
    <div style="padding-top: 50px">

    {{ info }}

      <v-container>
        
        <v-row v-for dense>
          <v-col
          >
            <v-card>
              <line-chart/>
            </v-card>
          </v-col>

          <v-col
          >
            <v-card>
              <line-chart/>
            </v-card>
          </v-col>
        </v-row>

        <!-- ########## -->

         <v-row dense>
          <v-col
          >
            <v-card>
              <line-chart/>
            </v-card>
          </v-col>

          <v-col
          >
            <v-card>
              <line-chart/>
            </v-card>
          </v-col>
        </v-row>

      </v-container>


    </div>
  </v-app>

</template>

<script>
import axios from 'axios';
import lineChart from "@/components/analytics/lineChart";
import BarChart from "@/components/analytics/barChart";

export default {
  name: "analytics",
  components: {BarChart, lineChart},
  data () {
    return {
      country: "Singapore",

      row1: [
      {
        "title": "Consumer Price Index, All items",
        "description": "The Consumer Price Index provides a comprehensive means to benchmark buying habits of urban consumers.",
        "years": [
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018",
          "2019"
        ],
        "value": [
          76.877,
          77.61725,
          79.251,
          84.5035833333333,
          85.0078333333333,
          87.4081666666667,
          91.9951666666667,
          96.2045,
          98.4735833333333,
          99.4830833333333,
          98.9631666666667,
          98.4364166666667,
          99.0036666666667,
          99.4379166666667,
          100
        ]
      },
      {
        "title": "Financial Development Index",
        "description": "The Financial Development Index provides a comprehensive means for economies to benchmark various aspects of their financial systems.",
        "years": [
          "2000",
          "2001",
          "2002",
          "2003",
          "2004",
          "2005",
          "2006",
          "2007",
          "2008",
          "2009",
          "2010",
          "2011",
          "2012",
          "2013",
          "2014",
          "2015",
          "2016",
          "2017",
          "2018"
        ],
        "value": [
          0.724017143249512,
          0.771380543708801,
          0.766390144824982,
          0.760503888130188,
          0.735540986061096,
          0.708265423774719,
          0.717682719230652,
          0.754076480865479,
          0.796741485595703,
          0.722230732440948,
          0.711304545402527,
          0.709599435329437,
          0.697518169879913,
          0.712999999523163,
          0.701376616954803,
          0.708463311195374,
          0.713519692420959,
          0.744822144508362,
          0.7528315782547
        ]
      }],

      row2: null,
      info: null
    }
  },
  mounted () {
    axios
      .get('http://lzl.blue/api/charts/' + this.country)
      .then(response => {
        this.info = response
    })
  }
};
</script>

<style scoped>

</style>
