<script>
import { Bar } from 'vue-chartjs'

export default {
  
  name: "barChart",
  
  extends: Bar,
  
  props: ["chartData"],

  // First time load chart
  mounted() {
    this.renderBarChart();
  },
  
  methods: {

    renderBarChart: function() {
      let colour_code = ["#2d4059", "#f07b3f", "#ffd460", "#ea5455"]
      let datasets_arr = []
      let size_arr = JSON.parse(JSON.stringify(this.chartData.regions)).length

      for (let i=0; i < size_arr; i++) {
        datasets_arr.push({
            fill: false,
            label: JSON.parse(JSON.stringify(this.chartData.regions))[i],
            backgroundColor: colour_code[i],
            borderColor: colour_code[i],
            borderWidth: 1,
            data: JSON.parse(JSON.stringify(this.chartData.value))[i]
        })
      }

      let obj = {
          labels: JSON.parse(JSON.stringify(this.chartData.years)),
          datasets: datasets_arr
        }

      let options = {
          maintainAspectRatio:false
        }
      this.renderChart(obj, options)
    }
  },


  // Watch prop change to re-render chart
  watch: {
    chartData: function() {
      this.renderChart();
    }
  }

}

</script>