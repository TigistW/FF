from flask import Flask, Blueprint,jsonify, request
from chat import chat_lagchain, load_new_conv
import logging
import json
app = Flask(__name__)
main_bp2 = Blueprint('main', __name__)
main_bp = Blueprint('main', __name__)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

@main_bp2.route('/', methods=['GET'])
def index():
    return "200"


@main_bp2.route('/api', methods=['POST'])
def api_route():
    data = request.json
    response = {
        "data" : None,
        "error" : None
    }
    statusCode = 404
    
    try:
        address = request.headers['address']
        message = data['message']
        conversation = load_new_conv(address)
        output = conversation.predict(input=message)
        logging.info(output)
        response['data'] = json.loads(output)
        statusCode = 200
        
    except Exception as error:
        logging.error(error)
        response['error'] = {
        'message': f"{error}"
        }
        # response = error
        statusCode = 404
        
    print(response)
    return jsonify(response), statusCode

app.register_blueprint(main_bp2)
if __name__ == '__main__':
    app.run()


