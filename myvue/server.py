from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 允许跨域请求


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()  # 获取Vue发送的数据
    num1 = data['num1']
    num2 = data['num2']
    result = num1 + num2  # 加法计算

    response = {'result': result}  # 构造响应数据
    return jsonify(response)


if __name__ == '__main__':
    app.run()
