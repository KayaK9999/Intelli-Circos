<script setup lang="ts">
import { csvParse } from 'd3'
import { onMounted, ref, watch, watchEffect } from 'vue'
import { watchDebounced, watchPausable } from '@vueuse/core'
import _, { before } from 'lodash-es'
import { useFigureStore } from '@/stores/figure'

import { Circos } from '@/lib/circosJS/dist/circos.module'

// import { Circos } from '@/lib/circosJS/src/circos'
import type { ITrack, RawCircosData } from '@/lib/circos'
import { useDataStore } from '@/stores/data'

// const { Circos } = circosJS
const figure = useFigureStore()
const dataStore = useDataStore()

let CircosInstance: ReturnType<typeof Circos> | undefined

const el = ref<HTMLElement>()
async function render(config: ITrack[], remove = false) {
  console.log(config)
  console.log('rendering')
  if (!config || config.length === 0)
    return
  if (!CircosInstance) {
    CircosInstance = Circos({
      container: el.value,
    })
  }
  config.forEach(async (track) => {
    // get data
    let data: RawCircosData = []
    if (track.data) {
      // if (typeof track.data === 'string')
      //   data = dataStore.files.find(file => file.name === track.data)?.content as RawCircosData
      // else if (track.data instanceof Function)
      //   data = await track.data()
      // else
      //   data = track.data
      data = track.data.content
    }
    if (track.type === 'layout') {
      // @ts-expect-error 先忽略掉TS错
      CircosInstance.layout(data, track.config)
    } else if (track.type === 'chord') { 
      // @ts-expect-error 先忽略掉TS错
      CircosInstance['chords'](track.id, data, track.config)
    } else {
      // @ts-expect-error 先忽略掉TS错
      CircosInstance[track.type](track.id, data, track.config)
    }
  })
  // @ts-expect-error 先忽略掉TS错
  CircosInstance.render([], remove)
}
onMounted(() => {
  render(_.cloneDeep(figure.tracks))
})

watchEffect(() => {
  render(_.cloneDeep(figure.tracks), true)
})

// onMounted(() => {
//   const { pause: pauseFigureConfigWatch, resume: resumeFigureConfigWatch } = watchPausable(figure, () => {
//     pauseFigureConfigWatch()
//     render(_.cloneDeep(figure.tracks), true)
//     setTimeout(() => resumeFigureConfigWatch(), 0)
//     // resumeFigureConfigWatch()
//   }, {
//     deep: true,
//   })
//   // watchDebounced(() => figure.tracks, () => {
//   //   render(_.cloneDeep(figure.tracks), true)
//   // }, {
//   //   debounce: 100,
//   //   deep: true,
//   // })
// })
</script>

<template>
  <div ref="el" h-full w-full flex="~ items-center content-center" overflow-hidden p-4 class="dark:brightness-120 dark:invert-10" />
</template>
