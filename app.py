from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)

CORS(app)

@app.route('/',methods=['GET'])
def index():
	return app.send_static_file('index.html')

@app.route('/predictPrice', methods=['GET','POST'])
def predictPrice():
	request_data = request.get_json()
	predictedPrice = util.predictSellingPrice(request_data)
	return jsonify({ 'predicted_price': predictedPrice })


if __name__ == '__main__':
    app.run(debug=True)