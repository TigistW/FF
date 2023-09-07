from flask import Flask, Blueprint
from chat import chat
app = Flask(__name__)
main_bp2 = Blueprint('main', __name__)
@main_bp2.route('/', methods=['GET'])
def index():
    return "200"


@main_bp2.route('/api', methods=['GET'])
def api_route():
    return chat()

app.register_blueprint(main_bp2)
if __name__ == '__main__':
    app.run()


