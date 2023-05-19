<template>
  <div class="calculator">
    <div class="display">
      <input v-model="num1" type="number" placeholder="Number 1">
      <input v-model="num2" type="number" placeholder="Number 2">
    </div>
    <div class="operators">
      <button @click="operator = '+'">+</button>
      <button @click="operator = '-'">-</button>
      <button @click="operator = '*'">*</button>
      <button @click="operator = '/'">/</button>
    </div>
    <div class="calculate">
      <button @click="calculate">Calculate</button>
    </div>
    <div v-if="result !== null" class="result">Result: {{ result }}</div>
  </div>
</template>

<style scoped>
.calculator {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

.display {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.display input {
  width: 100px;
  padding: 5px;
  margin: 0 10px;
}

.operators {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.operators button {
  margin: 0 5px;
  padding: 5px 10px;
}

.calculate {
  display: flex;
  justify-content: center;
}

.calculate button {
  padding: 10px 20px;
  font-size: 16px;
  font-weight: bold;
}

.result {
  margin-top: 20px;
  font-size: 18px;
  font-weight: bold;
}
</style>

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
