from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # 获取Vue发送的数据
    num1 = data['num1']
    num2 = data['num2']
    operator = data['operator']  # 获取运算符

    if operator == '+':
        result = num1 + num2  # 加法计算
    elif operator == '-':
        result = num1 - num2  # 减法计算
    elif operator == '*':
        result = num1 * num2  # 乘法计算
    elif operator == '/':
        if num2 == 0:
            return jsonify({'error': 'Division by zero'})  # 处理除数为零的情况
        result = num1 / num2  # 除法计算
    else:
        return jsonify({'error': 'Invalid operator'})  # 处理无效运算符的情况

    response = {'result': result}  # 构造响应数据
    return jsonify(response)


if __name__ == '__main__':
    app.run()
