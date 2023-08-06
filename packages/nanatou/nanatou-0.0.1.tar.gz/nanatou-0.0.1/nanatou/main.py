import requests

def rq():
    r = requests.post('http://httpbin.org/post', data = {'key':'value'})
    return r
