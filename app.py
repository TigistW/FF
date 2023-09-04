from flask import Flask, Blueprint

app = Flask(__name__)
main_bp2 = Blueprint('main', __name__)
@main_bp2.route('/', methods=['GET'])
def index():
    return "200"

app.register_blueprint(main_bp2)
if __name__ == '__main__':
    app.run()


