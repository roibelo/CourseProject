import requests

try:
    requests.get('http://127.0.0.1:6000/stop_server')
except Exception as ex:
    print(ex.__str__())


try:
    requests.get('http://127.0.0.1:6001/stop_server')
except Exception as ex:
    print(ex.__str__())