from behave import *
import requests
import json


def request(method, url, body=None, headers=None):
    """
    :param method: Should be equal to 'GET' or 'POST'
    :param url: The url that will be called
    :param body: Should be supplied as this format { "key1": "value1", "key2": "value2" }
    :param headers: Should be supplied as this format { "header1": "value1", "header2": "value2" }
    :return: Will return the status call of the request, if an undefined method is passed, or a blank body supplied on
    a 'POST' request this function will return a string 'FAILED'. In your test step should assert that 'FAILED' was not
    returned.
    """

#    if method != 'GET':
#        headers = json.loads(headers)

    if method == 'GET':
        response = requests.get(url=url)
        return response
    elif method == 'POST':
        response = requests.post(url=url, data=body, headers=headers)
        return response
    elif method == 'PUT':
        response = requests.put(url=url, data=body, headers=headers)
        return response
    else:
        print(f'{method} has not been defined')
        return 'FAILED'


@fixture
def pre_reqs(context):
    ip_address = '127.0.0.1'
    port = '8880'
    endpoint = 'pre-processor/clear-data-and-status'
    method = 'Post'
    headers = {"accept": "application/json"}

    print(
        f'Before All Tests, clear any status: method: {method}, IP: {ip_address}, port: {port}, endpoint: {endpoint}, headers: {headers}')
    context.cmd = request(method=method, url=f'http://{ip_address}:{port}/{endpoint}', headers=headers)


def before_all(context):
    use_fixture(pre_reqs, context)
