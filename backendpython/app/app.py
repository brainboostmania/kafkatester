from flask import Flask, request, jsonify
from flask_cors import CORS

from containers import Container, Services, Validator
import views

container = Container()
services = Services()
validator = Validator()

app = Flask(__name__)
app.container = container
app.add_url_rule('/', 'index', views.index)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/hello')
def hello_world():
    return '<p>Hello, World!</p>'


@app.route('/api/send', methods=['POST'])
def produce_message():
    validation_info = validator.producer_validator().validate(request.json)
    if validation_info and not validation_info.get('success'):
        print("Errors in sending request")
        return jsonify(validation_info), 200
    return jsonify(services.producer_service().send_message(request.json)), 200


@app.route('/api/fetch', methods=['POST'])
def fetch_message():
    validation_info = validator.consumer_validator().validate(request.json)
    if validation_info and not validation_info.get('success'):
        return jsonify(validation_info), 200

    return jsonify(services.consumer_service().get_messages(request.json)), 200


if __name__ == '__main__':
    app.run(use_reloader=True, host='0.0.0.0')
