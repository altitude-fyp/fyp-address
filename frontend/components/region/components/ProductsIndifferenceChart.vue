
<script>
import { Line } from 'vue-chartjs'

export default {
  
  name: "lineChart",
  
  extends: Line,
  
  props: ["productsChartData"],

  // First time load chart
  mounted() {
    this.renderLineChart();
  },
  
  methods: {

    renderLineChart: function() {

      let colour_code = ["#2d4059", "#ea5455", "#f07b3f", "#ffd460"]
      let datasets_arr = []
      let size_arr = JSON.parse(JSON.stringify(this.productsChartData.graph_1.regions)).length
      
      for (let i=0; i < size_arr; i++) {
        datasets_arr.push({
            fill: false,
            label: JSON.parse(JSON.stringify(this.productsChartData.graph_1.regions))[i],
            backgroundColor: colour_code[i],
            borderColor: colour_code[i],
            borderWidth: 1,
            data: JSON.parse(JSON.stringify(this.productsChartData.graph_1["y-axis"]))[i]
        })
      }

      let obj = {
          labels: JSON.parse(JSON.stringify(this.productsChartData.graph_1["x-axis"])),
          datasets: datasets_arr
        }
      this.renderChart(obj)
    }
  },

  // Watch prop change to re-render chart
  watch: {
    productsChartData: function() {
      this.renderLineChart();
    }
  }

}

</script>