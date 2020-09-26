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
  // computed: {
  //   plotdata: function () {
  //     return {
  //       labels: this.chartdata.years,
  //       datasets: [
  //         {
  //           label: this.chartdata.title,
  //           backgroundColor: '#79f8b6',
  //           data: this.chartdata.value
  //         }
  //       ]
  //     }
  //   } 
  // },
  
  mounted () { 
    this.renderChart(this.chartdata)
  }
}

</script>
