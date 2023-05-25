import requests


def do_get_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.get(url)
        if res.ok:
            data = res.json()
            print("<H1 id='user'>" + data["user_name"][0] + "</H1>")
        else:
            print("<H1 id='error'>no such user " + str(user_id) + "</H1>")
    except Exception as ex:
        print("<H1 id='error'>error: " + ex.__str__() + "</H1>")


def do_post_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.post(url, json={"user_name": "John"})
        if res.ok:
            data = res.json()
            print("<H1 id='user'>" + data["user_added"] + "</H1>")
        else:
            print("<H1 id='error'>id already exists " + str(user_id) + "</H1>")
    except Exception as ex:
        print("<H1 id='error'>error: " + ex.__str__() + "</H1>")


def do_update_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.put(url, json={"user_name": "Roi"})
        if res.ok:
            data = res.json()
            print("<H1 id='user'>" + data["user_updated"] + "</H1>")
        else:
            print("<H1 id='error'>no such user " + str(user_id) + "</H1>")
    except Exception as ex:
        print("<H1 id='error'>error: " + ex.__str__() + "</H1>")


def do_delete_request(user_id):
    try:
        url = "http://127.0.0.1:5000/users/" + str(user_id)
        res = requests.delete(url)
        if res.ok:
            data = res.json()
            print("<H1 id='user'>" + data["user_deleted"] + "</H1>")
        else:
            print("<H1 id='error'>no such user " + str(user_id) + "</H1>")
    except Exception as ex:
        print("<H1 id='error'>error: " + ex.__str__() + "</H1>")


#do_post_request(123456)
#do_get_request(12345)
#do_update_request(123456)
#do_get_request(123456)
#do_delete_request(12345)
#do_get_request(12345)