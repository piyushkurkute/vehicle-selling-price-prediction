from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
	return app.send_static_file('index.html')

@app.route('/predictPrice', methods=['POST'])
def predictPrice():
	request_data = request.get_json()
	predictedPrice = util.predictSellingPrice(request_data)
	return jsonify({ 'predicted_price': predictedPrice })


if __name__ == '__main__':
    app.run()
