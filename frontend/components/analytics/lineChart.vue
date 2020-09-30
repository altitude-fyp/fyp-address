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
    let datasets_arr = []
    let size_arr = JSON.parse(JSON.stringify(this.chartdata.years)).length
    for (i=0; i < size_arr; i++) {
      datasets_arr.push({
          label: JSON.parse(JSON.stringify(this.chartdata.title)),
          backgroundColor: '#79f8b6',
          data: JSON.parse(JSON.stringify(this.chartdata.value))
      })
    }
    let obj = {
        labels: JSON.parse(JSON.stringify(this.chartdata.years)),
        // datasets: [
        //   {
        //     label: JSON.parse(JSON.stringify(this.chartdata.title)),
        //     backgroundColor: '#79f8b6',
        //     data: JSON.parse(JSON.stringify(this.chartdata.value))
        //   }
        // ]
        datasets: datasets_arr
      }
    console.log(obj)

    this.renderChart(obj)
  }
}

</script>
