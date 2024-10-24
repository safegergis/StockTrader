<template>
  <Line :data="data" :options="options" />
</template>

<script lang="ts">
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
)

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line vue/no-reserved-component-names
    Line,
  },
  props: {
    stockHistory: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      data: this.chartData(),
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false, // Hide legend since we only have one dataset
          },
        },
        scales: {
          y: {
            grid: {
              color: 'rgba(156, 163, 175, 0.1)', // Light gray grid lines
            },
            ticks: {
              color: '#9ca3af', // Gray-400 for axis labels
            },
          },
          x: {
            grid: {
              display: false, // Hide x grid lines
            },
            ticks: {
              color: '#9ca3af',
              maxRotation: 45,
            },
          },
        },
      },
    }
  },
  watch: {
    stockHistory: {
      handler() {
        this.data = this.chartData()
      },
      deep: true,
    },
  },
  methods: {
    chartData() {
      interface StockHistory {
        Date: string
        Close: number
      }
      const stockHistory = JSON.parse(this.stockHistory)
      const prices: number[] = []
      const labels: string[] = []
      stockHistory.forEach((data: StockHistory) => {
        labels.push(new Date(data['Date']).toLocaleDateString())
        prices.push(data['Close'])
      })
      return {
        labels: labels,
        datasets: [
          {
            data: prices,
            borderColor: '#10b981', // Emerald-500 color
            backgroundColor: 'rgba(16, 185, 129, 0.1)', // Transparent emerald
            borderWidth: 2,
            tension: 0.4, // Smooth line
            pointRadius: 0, // Hide points
            pointHoverRadius: 4, // Show points on hover
            pointHoverBackgroundColor: '#10b981',
            pointHoverBorderColor: '#fff',
            fill: true,
          },
        ],
      }
    },
  },
}
</script>
