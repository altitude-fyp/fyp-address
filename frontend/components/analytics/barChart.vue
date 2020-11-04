<script>
import { Bar } from 'vue-chartjs'

export default {
  
  name: "barChart",
  
  extends: Bar,
  
  props: ["top10ChartData"],

  // First time load chart
  mounted() {
    this.renderBarChart();
  },
  
  methods: {

    renderBarChart: function() {
      let colour_code = ["#2d4059", "#ea5455", "#f07b3f", "#ffd460"]
      let datasets_arr = []
      let size_arr = JSON.parse(JSON.stringify(this.top10ChartData.countries)).length

      let obj = {
          labels: JSON.parse(JSON.stringify(this.top10ChartData.countries)),
          datasets: [
            {
              label: "Score",
              fill: false,
              backgroundColor: "#2d4059",
              borderColor: "#2d4059",
              borderWidth: 1,
              data: JSON.parse(JSON.stringify(this.top10ChartData.value))
            }
          ]
        }
      let options = {
          maintainAspectRatio:false
        }
      this.renderChart(obj, options)
    }
  },


  // Watch prop change to re-render chart
  watch: {
    top10Chartdata: function() {
      this.renderChart();
    }
  }

}

</script>