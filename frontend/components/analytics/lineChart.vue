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
    let size_arr = JSON.parse(JSON.stringify(this.chartdata.countries)).length
    for (let i=0; i < size_arr; i++) {
      datasets_arr.push({
          label: JSON.parse(JSON.stringify(this.chartdata.countries))[i],
          backgroundColor: colour_code[i],
          data: JSON.parse(JSON.stringify(this.chartdata.value))[i]
      })
    }
    console.log(datasets_arr)
    let obj = {
        labels: JSON.parse(JSON.stringify(this.chartdata.years)),
        datasets: datasets_arr
      }
    console.log(JSON.parse(JSON.stringify(obj)))
    this.renderChart(obj)
  }
}

</script>
