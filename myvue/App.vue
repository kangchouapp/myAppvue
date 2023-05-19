<template>
  <div>
    <input v-model="num1" type="number" placeholder="Number 1"> <!-- 输入框，绑定到 num1 变量 -->
    <input v-model="num2" type="number" placeholder="Number 2"> <!-- 输入框，绑定到 num2 变量 -->
    <button @click="calculate">点击输出计算结果</button> <!-- 点击按钮触发 calculate 方法 -->
    <div v-if="result !== null">Result: {{ result }}</div> <!-- 显示结果，仅当 result 不为 null 时显示 -->
  </div>
</template>

<script>
export default {
  data() {
    return {
      num1: 0, // 存储第一个数的变量
      num2: 0, // 存储第二个数的变量
      result: null, // 存储计算结果的变量
    };
  },
  methods: {
    calculate() { // 计算方法
      const data = {
        num1: parseInt(this.num1),  // 将输入的字符串转为整数
        num2: parseInt(this.num2),  // 将输入的字符串转为整数
      };

      fetch('http://localhost:5000/calculate', { // 发送计算请求到服务器
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data), // 将数据转为 JSON 字符串并作为请求体发送
      })
        .then((response) => response.json()) // 解析响应为 JSON 格式
        .then((data) => {
          this.result = data.result; // 将服务器返回的计算结果存储到 result 变量中
        })
        .catch((error) => {
          console.error('Error:', error); // 打印错误信息
        });
    },
  },
};
</script>
