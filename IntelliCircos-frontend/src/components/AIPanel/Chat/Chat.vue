<script setup lang="ts">
import ChatHeader from './ChatHeader.vue'
import ChatTextArea from './ChatTextArea.vue'
import ChatBubble from './ChatBubble.vue'
import { Card, CardContent, CardFooter, CardHeader } from '@/components/ui/card'
import { useChat } from '@/lib/ai/client'

const { messages, reloadMessage } = useChat()
messages.value = [
  {
    id: -1,
    text: 'Hello, how can I help you?',
    role: 'agent',
    lastUpdated: Date.now(),
  },
  // {
  //   id: 0,
  //   text: 'Karyotype Data includes: human and mouse;\n Attachments Data includes: both.cons.2e6.avg, both.cons.2e6.danrer.avg, both.cons.2e6.fr.avg, both.cons.2e6.max, both.cons.2e6.min, both.cons.2e6.rhe.avg, both.cons.2e6.rn.avg, links, links.density and tiles.\n Compare their gene conversation scores and the homology relationship between genes, and display the sampling situation of gene sequencing.',
  //   role: 'user',
  //   lastUpdated: Date.now(),
  // },
  // {
  //   id: 1,
  //   text: 'the <ideogram> track displays genomic information, the <highlight> track shows gene conservation scores, the <histogram> track displays homology relation- ships, the <scatter> track shows the sampling information of gene sequencing, the <chord> track illustrates relationships between genomic data',
  //   role: 'agent',
  //   lastUpdated: Date.now(),
  //   code: '<ideogram><split><highlight><split><histogram><split><scatter><split><chord>',
  //   reference: [
  //     {
  //       title: '10.1371_journal.pone.0161369.pdf',
  //       url: 'intellicircos/10.1371_journal.pone.0161369.pdf/page_5',
  //     },
  //     {
  //       title: '10.1371_journal.pone.0161369.pdf',
  //       url: 'intellicircos/10.1371_journal.pone.0161369.pdff/page_6',
  //     },
  //     {
  //       title: '10.1016_j.cancergen.2014.11.003.pdf.pdf',
  //       url: 'intellicircos/10.1016_j.cancergen.2014.11.003.pdf.pdf/page_8',
  //     },
  //     {
  //       title: '10.1186_s12885-015-1077-4.pdf',
  //       url: 'intellicircos/10.1186_s12885-015-1077-4.pdf.pdf/page_',
  //     }
  //   ],
  // },
  // {
  //   id: 2,
  //   text: 'The sampling profile of genes refers to gene segments measured in high-throughput sequencing and is used to show coverage of gene locations, please recommend the new view type for this data type',
  //   role: 'user',
  //   lastUpdated: Date.now(),
  // },
  // {
  //   id: 3,
  //   text: 'Sorry, I misunderstood your request. I suggest using a <tile> track instead of a <scatter> track as it can display overlapping ranges effectively.',
  //   role: 'agent',
  //   lastUpdated: Date.now(),
  //   code: '<ideogram><split><highlight><split><histogram><split><tile><split><chord>',
  //   reference: [
  //     {
  //       title: '10.1186_s13020-021-00460-z.pdf',
  //       url: 'intellicircos/10.1186_s13020-021-00460-z.pdf/page_5',
  //     },
  //     {
  //       title: '10.1371_journal.pone.0074132.pdf',
  //       url: 'intellicircos/10.1371_journal.pone.0074132.pdf/page_6',
  //     },
  //     {
  //       title: '10.1007_s11816-021-00682-5.pdf',
  //       url: 'intellicircos/10.1007_s11816-021-00682-5.pdf/page_8',
  //     },
  //     {
  //       title: '10.1186_s13020-021-00460-z.pdf',
  //       url: 'intellicircos/10.1186_s13020-021-00460-z.pdf/page_',
  //     }
  //   ],
  // },
]
</script>

<template>
  <Card class="h-full flex flex-col">
    <CardHeader class="border-b py-2">
      <ChatHeader />
    </CardHeader>
    <CardContent class="flex-1 overflow-auto py-2">
      <div className="space-y-4">
        <ChatBubble
          v-for="message in messages"
          :key="message.id"
          :text="message.text"
          :role="message.role"
          :loading="message.loading"
          :code="message.code"
          :reference="message.reference"
          @reload="() => reloadMessage(message.id)"
        />
      </div>
    </CardContent>
    <CardFooter border-t="~" class="p-4">
      <ChatTextArea />
    </CardFooter>
  </Card>
</template>
