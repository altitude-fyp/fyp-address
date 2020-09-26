<template>
  <v-app>
    <div style="padding-top: 50px">

    {{ info }}

      <v-container>
        
        <v-row dense>
          <v-col>
            <v-card>
              <line-chart
                v-if="loaded"
                :chartdata="childdata.plotdata"
              />
            </v-card>
          </v-col>
        </v-row>

        <!-- ############################ -->

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

  data: () => ({
    country: "Singapore",
    loaded: false,
    chartdata: null,
    childdata: []
  }),
  mounted () {
    this.loaded = false
    try {
      axios.get('http://lzl.blue/api/charts/'  + this.country).then(response => {
        this.chartdata = JSON.parse(JSON.stringify(response))

        console.log(this.chartdata)
        console.log(typeof this.chartdata)


        this.loaded = true
        this.chartdata.forEach(data => {
          let obj = {
            plotdata : {
              labels: data.years,
              datasets: [
                {
                  label: data.title,
                  backgroundColor: '#79f8b6',
                  data: data.value
                }
              ]
            },
            description: data.description
          }
          this.childdata.push(obj)
        })
      })

      
    } catch (e) {
      console.error(e)
    }
  },

  methods: {
    handleData(apiData) {
     apiData.forEach(data => {
        let obj = {
          plotdata : {
            labels: data.years,
            datasets: [
              {
                label: data.title,
                backgroundColor: '#79f8b6',
                data: data.value
              }
            ]
          },
          description: data.description
        }
        this.childdata.push(obj)
      })
    }
  }

};
</script>

<style scoped>

</style>
