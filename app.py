from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import requests

app = Flask(__name__)


class Addition(Resource):
    def post(self):
        numbers = request.form.to_dict()
        num = []
        # Append the dateRange(Dict) value into dateList
        for key, value in numbers.items():
            temp = value
            num.append(temp)
        num1 = int(num[0])
        num2 = int(num[1])
        result = num1 + num2
        return jsonify(result=result)


api = Api(app)
api.add_resource(Addition, '/api/addition')


@app.route('/')
def add():
    num1 = 100
    num2 = 200
    response = requests.post("http://127.0.0.1:5000/api/reports",
                             data={'num1': num1,
                                   'num2': num2})
    r_json = response.json()
    result = r_json['result']
    return jsonify(result=result)


if __name__ == "__main__":
    app.run()
