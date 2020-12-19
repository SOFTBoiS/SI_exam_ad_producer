from flask import Flask, request, jsonify
import grpc_client

app = Flask(__name__)


@app.route('/test')
def hello_world():
    return 'Hello, World!'


@app.route('/produce-ads', methods=['POST'])
def foo():
    try:
        data = request.json
        res = grpc_client.get_email()
        return f"{res} emails sent", 200
    except Exception as ex:
        print(ex)
        return "Invalid query. Check your values", 403
