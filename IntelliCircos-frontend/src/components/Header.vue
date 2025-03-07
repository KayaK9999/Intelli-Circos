<script setup lang="ts">
import { Moon, PanelRightClose, PanelRightOpen, Sun, ArrowDownToLine } from 'lucide-vue-next'
import { useDark, useToggle } from '@vueuse/core'
import { Button } from '@/components/ui/button'
import { useLayoutStore } from '@/stores/layout'
import { useFigureStore } from '@/stores/figure'

const figureStore = useFigureStore()

const download = function () {
  // 创建一个 SVG 内容
  const svgContent = `
      <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />
      </svg>
  `;
  // 创建一个 Blob 对象来存储 SVG 内容
  const blob = new Blob([svgContent], { type: 'image/svg+xml' });

  // 创建一个下载链接
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "circos.svg";  // 设置下载文件的默认名称
  // 触发下载
  link.click();
}

const isDark = useDark()
const toggleDark = useToggle(isDark)

const layoutStore = useLayoutStore()
</script>

<template>
  <header class="h-[50px] flex items-center border bg-background px-2 py-1 lg:px-4">
    <div class="flex items-center overflow-hidden">
      <img class="mx-2" alt="IntelliCircos logo" src="../assets/LOGO-Large.svg" width="36" height="36">
      <span class="text-xl text-foreground-foreground font-medium font-rounded">Intelli</span>
      <span class="text-xl text-[#E41279] font-rounded">Circos</span>
    </div>
    <div class="flex-1" />
    <div class="flex items-center gap-1 text-primary">
      <Button variant="outline" size="icon" @click="download()">
        <ArrowDownToLine class="h-5 w-5" :stroke-width="2" />
      </Button>
      <Button variant="outline" size="icon" @click="toggleDark()">
        <Transition>
          <Sun v-if="!isDark" class="h-5 w-5" :stroke-width="2" />
          <Moon v-else class="h-5 w-5" :stroke-width="2" />
        </Transition>
      </Button>

      <Button variant="outline" size="icon" @click="() => layoutStore.toggleRightPanel()">
        <Transition enter-active-class=" duration-300 ease-in-out" enter-from-class="transform rotate-180"
          enter-to-class="transform rotate-0" mode="out-in">
          <PanelRightClose v-if="layoutStore.rightPanelOpen" class="h-5 w-5" :stroke-width="2" />
          <PanelRightOpen v-else class="h-5 w-5" :stroke-width="2" />
        </Transition>
      </Button>
    </div>
  </header>
</template>
