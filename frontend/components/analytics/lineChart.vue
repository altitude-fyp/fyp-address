<script>
import { Line } from 'vue-chartjs'

export default {
  name: "lineChart",
  extends: Line,
  props: {
    chartdata: {
      type: Object,
      default: null
    }
  },

  mounted() {  
    let colour_code = ["#2d4059", "#ea5455", "#f07b3f", "#ffd460"]
    let obj = {
        labels: JSON.parse(JSON.stringify(this.chartdata.years)),
        datasets: [
          {
            label: JSON.parse(JSON.stringify(this.chartdata.title)),
            backgroundColor: '#79f8b6',
            data: JSON.parse(JSON.stringify(this.chartdata.value))
          }
        ]
      }
    console.log(obj)

    this.renderChart(obj)
  }
}

</script>
