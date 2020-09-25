<script>
import { Bar } from 'vue-chartjs'

export default {
  name: "barChart",
  extends: Bar,
  data: () => ({
    chartdata: {
      labels: ['lABEL 1', 'Label 2'],
      datasets: [
        {
          label: 'Data One',
          backgroundColor: '#79f8b6',
          data: [40, 20]
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false
    }
  }),

  mounted () {
    this.renderChart(this.chartdata, this.options)
  }
}
</script>
