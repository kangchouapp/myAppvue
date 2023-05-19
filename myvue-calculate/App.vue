<template>
  <div>
    <input v-model="num1" type="number" placeholder="Number 1">
    <input v-model="num2" type="number" placeholder="Number 2">
    <select v-model="operator">
      <option value="+">加法</option>
      <option value="-">减法</option>
      <option value="*">乘法</option>
      <option value="/">除法</option>
    </select>
    <button @click="calculate">Calculate</button>
    <div v-if="result !== null">Result: {{ result }}</div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      num1: 0,
      num2: 0,
      operator: '+',  // 默认运算符为加号
      result: null,
    };
  },
  methods: {
    calculate() {
      const data = {
        num1: parseInt(this.num1),
        num2: parseInt(this.num2),
        operator: this.operator,  // 将运算符添加到发送的数据中
      };

      fetch('http://localhost:5000/calculate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then((response) => response.json())
        .then((data) => {
          this.result = data.result;
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    },
  },
};
</script>
