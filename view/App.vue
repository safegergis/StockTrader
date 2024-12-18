<script setup lang="ts">
import type { DateRange } from 'radix-vue'
import {
  Calendar as CalendarIcon,
  Download as DownloadIcon,
  Play as PlayIcon,
} from 'lucide-vue-next'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from '@/components/ui/popover'
import {
  Select,
  SelectContent,
  SelectGroup,
  SelectItem,
  SelectLabel,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select'
import { RangeCalendar } from '@/components/ui/range-calendar'
import { cn } from '@/lib/utils'
import ThemeSwitch from '@/components/ThemeSwitch.vue'
import {
  CalendarDate,
  DateFormatter,
  getLocalTimeZone,
} from '@internationalized/date'
import { ref, type Ref } from 'vue'
import { ofetch } from 'ofetch'
import StockChart from '@/components/StockChart.vue'
import download from 'downloadjs'

const df = new DateFormatter('en-US', {
  dateStyle: 'medium',
})
const dateRange = ref({
  start: new CalendarDate(2020, 1, 1),
  end: new CalendarDate(2024, 10, 24),
}) as Ref<DateRange>
const symbol = ref('')
const renderChart = ref(false)
const stockHistory = ref('')
const initialBalance = ref(0)
const finalBalance = ref(0)
const totalGainLoss = ref(0)
const totalTrades = ref(0)
const totalReturn = ref(0)
const strategy = ref('')
const fetchSymbolHistory = async () => {
  console.log(symbol.value, dateRange.value.start, dateRange.value.end)
  if (symbol.value && dateRange.value.start && dateRange.value.end) {
    await ofetch(
      `http://localhost:5000/fetch_history?symbol=${symbol.value}&start_date=${dateRange.value.start}&end_date=${dateRange.value.end}`,
    ).then(res => {
      localStorage.setItem('symbolHistory', res)
      stockHistory.value = res
      download(res, 'stock_history.json', 'text/plain')
      renderChart.value = true
    })
  }
}
const runBacktest = async () => {
  if (stockHistory.value) {
    await ofetch(`http://localhost:5000/${strategy.value}_backtest`, {
      method: 'POST',
      body: stockHistory.value,
    }).then(res => {
      console.log(res[1])
      download(res[0], 'backtest_results.json', 'text/plain')
      const metrics = JSON.parse(res[1])
      initialBalance.value = metrics.initial_balance
      finalBalance.value = metrics.final_balance
      totalGainLoss.value = metrics.total_gain_loss
      totalTrades.value = metrics.total_trades
      totalReturn.value = metrics.total_return
    })
  }
}
</script>

<template>
  <div
    class="flex align-center justify-center gap-4 p-4 dark:bg-gray-900 min-h-screen"
  >
    <div class="flex flex-col gap-4 p-4">
      <div class="flex items-center gap-4">
        <Select v-model="symbol">
          <SelectTrigger
            class="w-[180px] dark:bg-gray-800 dark:border-gray-700"
          >
            <SelectValue
              placeholder="Select symbol"
              class="dark:text-gray-200"
            />
          </SelectTrigger>
          <SelectContent class="dark:bg-gray-800 dark:border-gray-700">
            <SelectGroup>
              <SelectLabel class="dark:text-gray-400"
                >Trading Symbols</SelectLabel
              >
              <SelectItem value="FNGU" class="dark:text-gray-200"
                >FNGU</SelectItem
              >
              <SelectItem value="FNGD" class="dark:text-gray-200"
                >FNGD</SelectItem
              >
            </SelectGroup>
          </SelectContent>
        </Select>

        <Popover>
          <PopoverTrigger as-child>
            <Button
              variant="outline"
              class="dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
              :class="
                cn(
                  'w-[280px] justify-start text-left font-normal',
                  !dateRange && 'text-muted-foreground',
                )
              "
            >
              <CalendarIcon class="mr-2 h-4 w-4" />

              <template v-if="dateRange.start">
                <template v-if="dateRange.end">
                  {{ df.format(dateRange.start.toDate(getLocalTimeZone())) }} -
                  {{ df.format(dateRange.end.toDate(getLocalTimeZone())) }}
                </template>
                <template v-else>
                  {{ df.format(dateRange.start.toDate(getLocalTimeZone())) }}
                </template>
              </template>
              <template v-else>
                <span class="text-gray-400">pick a date range</span>
              </template>
            </Button>
          </PopoverTrigger>
          <PopoverContent
            class="w-auto p-0 dark:bg-gray-800 dark:border-gray-700"
          >
            <RangeCalendar
              mode="range"
              initialFocus
              class="dark:bg-gray-800 dark:text-gray-200"
              v-model="dateRange"
              :min-value="new CalendarDate(2020, 1, 1)"
            />
          </PopoverContent>
        </Popover>

        <Button
          variant="outline"
          class="dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
          @click="fetchSymbolHistory()"
        >
          <DownloadIcon class="mr-2 h-4 w-4" />
          Download Results
        </Button>
        <ThemeSwitch />
      </div>

      <div
        class="w-full h-[500px] border rounded-lg bg-card p-4 flex items-center justify-center text-muted-foreground dark:border-gray-700 dark:bg-gray-800 dark:text-gray-400"
      >
        <StockChart v-if="renderChart" :stock-history="stockHistory" />
      </div>

      <div class="grid grid-cols-2 gap-4">
        <Card class="dark:bg-gray-800 dark:border-gray-700">
          <CardHeader>
            <CardTitle class="dark:text-gray-200"
              >Performance Metrics</CardTitle
            >
          </CardHeader>
          <CardContent class="grid grid-cols-2 gap-4">
            <div>
              <Select v-model="strategy">
                <SelectTrigger
                  class="w-[180px] dark:bg-gray-800 dark:border-gray-700"
                >
                  <SelectValue
                    placeholder="Select trading strategy"
                    class="dark:text-gray-200"
                  />
                </SelectTrigger>
                <SelectContent class="dark:bg-gray-800 dark:border-gray-700">
                  <SelectGroup>
                    <SelectLabel class="dark:text-gray-400"
                      >Trading Strategies</SelectLabel
                    >
                    <SelectItem value="sma" class="dark:text-gray-200"
                      >SMA</SelectItem
                    >
                    <SelectItem value="bb" class="dark:text-gray-200"
                      >BB</SelectItem
                    >
                    <SelectItem value="macd" class="dark:text-gray-200"
                      >MACD</SelectItem
                    >
                  </SelectGroup>
                </SelectContent>
              </Select>
              <Button
                variant="default"
                class="dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-gray-200 mt-4"
                @click="runBacktest()"
              >
                <PlayIcon class="mr-2 h-4 w-4" />
                Run Backtest
              </Button>
            </div>
            <div>
              <div class="grid grid-cols-2 gap-4">
                <div class="space-y-2">
                  <p class="text-sm text-muted-foreground dark:text-gray-400">
                    Initial Balance
                  </p>
                  <p class="text-2xl font-bold dark:text-gray-200">
                    ${{ initialBalance?.toLocaleString() ?? '---' }}
                  </p>
                </div>
                <div class="space-y-2">
                  <p class="text-sm text-muted-foreground dark:text-gray-400">
                    Total Gain/Loss
                  </p>
                  <p
                    class="text-2xl font-bold"
                    :class="
                      totalGainLoss > 0 ? 'text-green-500' : 'text-red-500'
                    "
                  >
                    ${{ totalGainLoss?.toLocaleString() ?? '---' }}
                  </p>
                </div>
                <div class="space-y-2">
                  <p class="text-sm text-muted-foreground dark:text-gray-400">
                    Total Trades
                  </p>
                  <p class="text-2xl font-bold dark:text-gray-200">
                    {{ totalTrades ?? '---' }}
                  </p>
                </div>
                <div class="space-y-2">
                  <p class="text-sm text-muted-foreground dark:text-gray-400">
                    Total Return
                  </p>
                  <p
                    class="text-2xl font-bold"
                    :class="totalReturn > 0 ? 'text-green-500' : 'text-red-500'"
                  >
                    {{ totalReturn ? `${totalReturn.toFixed(2)}%` : '---' }}
                  </p>
                </div>
                <div class="space-y-2">
                  <p class="text-sm text-muted-foreground dark:text-gray-400">
                    Final Balance
                  </p>
                  <p class="text-2xl font-bold dark:text-gray-200">
                    ${{ finalBalance?.toLocaleString() ?? '---' }}
                  </p>
                </div>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  </div>
</template>

<style scoped></style>
