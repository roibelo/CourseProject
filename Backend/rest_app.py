import os
import signal
from flask import Flask, request
#from Dal import db_connector

app = Flask(__name__)

# local users storage
users = {}
# supported methods


@app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    if request.method == 'GET':
        # return {'user_id': user_id, 'user_name': users[user_id]}, 200 # status code
        try:
            from Dal import db_connector
            user_name = db_connector.get_user_name(user_id)
            if user_name != "":
                return {'status': 'ok', 'user_name': user_name}, 200  # status code
            else:
                return {'status': 'error', 'reason': 'no such id'}, 500  # status code
        except Exception as ex:
            return {'status': 'error', 'reason': ex.__str__()}, 500  # status code

    elif request.method == 'POST':
        try:
            from Dal import db_connector
            request_data = request.json
            user_name = request_data.get('user_name')
            user_name = db_connector.insert_user(user_id, user_name)
            return {'status': 'ok', 'user_added': user_name}, 200  # status code
        except Exception as ex:
            return {'status': 'error', 'reason': 'id already exists'}, 500  # status code

    elif request.method == 'PUT':
        try:
            from Dal import db_connector
            request_data = request.json
            user_name = request_data.get('user_name')
            user_name = db_connector.update_user(user_id, user_name)
            return {'status': 'ok', 'user_updated': user_name}, 200  # status code
        except Exception as ex:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code

    elif request.method == 'DELETE':
        try:
            from Dal import db_connector
            user_id = db_connector.delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except Exception as ex:
            return {'status': 'error', 'reason': 'no such id'}, 500  # status code


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


app.run(host='127.0.0.1', debug=True, port=5000)
os.kill(os.getpid(), signal.CTRL_C_EVENT)