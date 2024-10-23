<script setup lang="ts">
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
</script>

<template>
  <div class="flex flex-col gap-4 p-4 dark:bg-gray-900">
    <div class="flex items-center gap-4">
      <Select>
        <SelectTrigger class="w-[180px] dark:bg-gray-800 dark:border-gray-700">
          <SelectValue placeholder="Select symbol" />
        </SelectTrigger>
        <SelectContent>
          <SelectGroup>
            <SelectLabel>Trading Symbols</SelectLabel>
            <SelectItem value="FNGU">FNGU</SelectItem>
            <SelectItem value="FNGD">FNGD</SelectItem>
          </SelectGroup>
        </SelectContent>
      </Select>

      <Popover>
        <PopoverTrigger as-child>
          <Button
            variant="outline"
            class="dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
          >
            <CalendarIcon class="mr-2 h-4 w-4" />
            Pick a date range
          </Button>
        </PopoverTrigger>
        <PopoverContent
          class="w-auto p-0 dark:bg-gray-800 dark:border-gray-700"
        >
          <RangeCalendar
            mode="range"
            initialFocus
            class="dark:bg-gray-800 dark:text-gray-200"
          />
        </PopoverContent>
      </Popover>

      <Button
        variant="outline"
        class="dark:bg-gray-800 dark:border-gray-700 dark:text-gray-200"
      >
        <DownloadIcon class="mr-2 h-4 w-4" />
        Download Results
      </Button>
    </div>

    <div
      class="w-full h-[400px] border rounded-lg bg-card p-4 flex items-center justify-center text-muted-foreground"
    >
      Chart will be rendered here
    </div>

    <div class="grid grid-cols-2 gap-4">
      <Card>
        <CardHeader>
          <CardTitle>Performance Metrics</CardTitle>
        </CardHeader>
        <CardContent class="grid grid-cols-2 gap-4">
          <div>
            <Select>
              <SelectTrigger class="w-[180px]">
                <SelectValue placeholder="Select trading strategy" />
              </SelectTrigger>
              <SelectContent>
                <SelectGroup>
                  <SelectLabel>Trading Strategies</SelectLabel>
                  <SelectItem value="placeholder">placeholder</SelectItem>
                </SelectGroup>
              </SelectContent>
            </Select>
            <Button
              variant="default"
              class="dark:bg-gray-700 dark:hover:bg-gray-600 dark:text-gray-200 mt-4"
            >
              <PlayIcon class="mr-2 h-4 w-4" />
              Run Backtest
            </Button>
          </div>
          <div>
            <div class="grid grid-cols-2 gap-4">
              <div class="space-y-2">
                <p class="text-sm text-muted-foreground">Total Gain/Loss</p>
                <p class="text-2xl font-bold text-green-500">$12,450.00</p>
              </div>
              <div class="space-y-2">
                <p class="text-sm text-muted-foreground">Annual Return</p>
                <p class="text-2xl font-bold">24.5%</p>
              </div>
              <div class="space-y-2">
                <p class="text-sm text-muted-foreground">Total Return</p>
                <p class="text-2xl font-bold">45.8%</p>
              </div>
              <div class="space-y-2">
                <p class="text-sm text-muted-foreground">Current Balance</p>
                <p class="text-2xl font-bold">$45,670.00</p>
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Strategy Parameters</CardTitle>
        </CardHeader>
        <CardContent>
          <div class="space-y-4">
            <div class="grid grid-cols-2 gap-4">
              <div class="space-y-2">
                <Label>Moving Average Period</Label>
                <Input type="number" placeholder="20" />
              </div>
              <div class="space-y-2">
                <Label>Standard Deviation</Label>
                <Input type="number" placeholder="2" />
              </div>
            </div>
            <Button class="w-full">Update Parameters</Button>
          </div>
        </CardContent>
      </Card>
    </div>
  </div>
</template>

<style scoped></style>
