<template>
  <div>
    <h1>{{ msg }}</h1>

    <!-- 按钮，点击后使 count 自增 -->
    <button @click="state.count++">count is: {{ state.count }}</button>
    
    <!-- 显示从 API 获取的 text1 数据 -->
    <p>{{ data.text1 }}</p>
    
    <!-- 显示从 API 获取的 text2 数据 -->
    <p>{{ data.text2 }}</p>
    
    <!-- 显示 count 和 text1 作为数字之和 -->
    <p>Sum: {{ sum }}</p>
    
    <!-- 用户输入框，使用双向绑定将输入框值绑定到 userInput 变量 -->
    <input v-model="userInput" placeholder="Enter text">
    
    <!-- 显示拼接后的文本：用户输入 + text1 -->
    <p>Concatenated Text: {{ concatenatedText }}</p>
  </div>
</template>

<script setup>
import { defineProps, reactive, onMounted, computed, ref } from 'vue'

defineProps({
  msg: String
})

// 创建一个响应式对象来存储状态变量 count
const state = reactive({ count: 0 })

// 创建一个响应式对象来存储从 API 获取的数据 text1
const data = reactive({ text1: "" })

// 创建一个 ref 变量来存储用户输入的值
const userInput = ref("");

// 在组件挂载后执行的操作
onMounted(async () => {
  // 获取 API 数据并将其赋值给 data.text1
  const rsp1 = await fetch(`http://127.0.0.1:8010/hello`).then(rsp => rsp.text())
  data.text1 = rsp1 + '{dfvdthyj}'

  // 获取 API 数据并将其赋值给 data.text2
  const rsp2 = await fetch(`http://127.0.0.1:8010/hello`, {method: 'POST'}).then(rsp => rsp.text())
  data.text2 = rsp2
})

// 创建一个计算属性来计算 count 和 text1 作为数字之和
const sum = computed(() => {
  const text1AsNumber = parseInt(data.text1) || 0;
  return state.count + text1AsNumber;
});

// 创建一个计算属性来拼接用户输入和 text1
const concatenatedText = computed(() => {
  return `${userInput.value} ${data.text1}`;
});
</script>

<style scoped>
a {
  color: #42b983;
}
</style>
