import './assets/index.css'

import { createApp } from 'vue'
import App from './App.vue'

import CanvasJSStockChart from '@canvasjs/vue-stockcharts'

const app = createApp(App)
app.use(CanvasJSStockChart)
app.mount('#app')
