import json
import os
import signal

from flask import Flask
import requests

from Dal import db_connector

app = Flask(__name__)

# accessed via <HOST>:<PORT>/users/get_user_data/<user_id>
@app.route("/users/get_user_data/<user_id>")
def get_user_data(user_id):
    try:
        user_name = db_connector.get_user_name(user_id)
        if user_name != "":
            return "<H1 id='user'>" + user_name[0] + "</H1>"
        else:
            return "<H1 id='error'>no such user " + user_id + "</H1>"
    except Exception as ex:
        return "<H1 id='error'>error: " + ex.__str__() + "</H1>"


# accessed via <HOST>:<PORT>/users/post_user_data/<user_id>
@app.route("/users/post_user_data/<user_id>")
def post_user_data(user_id):

    try:
        user_name = db_connector.insert_user(user_id, "Roi")
        if user_name != "":
            return "<H1 id='user'>user: " + user_name + " as inserted</H1>"
        else:
            return "<H1 id='error'>no such user " + user_id + "</H1>"
    except Exception as ex:
        return "<H1 id='error'>error: " + ex.__str__() + "</H1>"


# accessed via <HOST>:<PORT>/users/update_user_data/<user_id>
@app.route("/users/update_user_data/<user_id>")
def update_user_data(user_id):

    try:
        user_name = db_connector.update_user(user_id, "Dasi")
        if user_name != "":
            return "<H1 id='user'>user id: " + user_id + " updated with the name " + user_name + "</H1>"
        else:
            return "<H1 id='error'>no such user " + user_id + "</H1>"
    except Exception as ex:
        return "<H1 id='error'>error: " + ex.__str__() + "</H1>"


# accessed via <HOST>:<PORT>/users/delete_user_data/<user_id>
@app.route("/users/delete_user_data/<user_id>")
def delete_user_data(user_id):

    try:
        db_connector.delete_user(user_id)
        return "<H1 id='user'>user id: " + user_id + " was deleted</H1>"
    except Exception as ex:
        return "<H1 id='error'>error: " + ex.__str__() + "</H1>"


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'


# host is pointing at local machine address
# debug is used for more detailed logs + hot swaping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)