<script lang="ts" setup>
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu'
import { useColorMode } from '@vueuse/core'
import { Moon, Sun } from 'lucide-vue-next'
const mode = useColorMode()
</script>
<template>
  <DropdownMenu>
    <DropdownMenuTrigger as-child>
      <Button variant="outline">
        <Moon
          class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
        />
        <Sun
          class="h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100 dark:text-gray-200"
        />
        <span class="sr-only">Toggle theme</span>
      </Button>
    </DropdownMenuTrigger>
    <DropdownMenuContent align="end">
      <DropdownMenuItem @click="mode = 'light'"> Light </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'dark'"> Dark </DropdownMenuItem>
      <DropdownMenuItem @click="mode = 'auto'"> System </DropdownMenuItem>
    </DropdownMenuContent>
  </DropdownMenu>
</template>
