from behave import *
from asserts import assert_true, assert_equal, assert_raises, assert_not_equal
import subprocess
import requests
import json


def os_cmd(command):
    p = subprocess.check_output(command, shell=True)
    return p.decode("utf-8")


def request(method, url, body=None, headers=None):
    """
    :param headers: Should be supplied as this format { "header1": "value1", "header2": "value2" }
    :param method: Should be equal to 'GET' or 'POST'
    :param url: The url that will be called
    :param body: Should be supplied as this format { "key1": "value1", "key2": "value2" }
    :return: Will return the status call of the request, if an undefined method is passed, or a blank body supplied on
    a 'POST' request this function will return a string 'FAILED'. In your test step should assert that 'FAILED' was not
    returned.
    """

    if method != 'GET':
        headers = json.loads(headers)

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


use_step_matcher("re")


@given("that docker compose is up and running")
def step_impl(context):
    """
    Run 'docker ps' command in terminal and verify docker has containers
    """
    cmd = os_cmd('docker ps')
    print(cmd)
    print(type(cmd))
    nlines = len(cmd.splitlines())
    print(nlines)

    assert_true(nlines > 1, msg_fmt=f"Expected line count to be Greater Than 1. Actual line count: {nlines}")


@when("the user sends a request to http://localhost:(?P<port>.+)")
def step_impl(context, port):
    """
    Use a requests library to send a request to http://localhost:<port>
    """
    context.cmd = request('GET', f'http://localhost:{port}')
    print(context.cmd)
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')


@then("the user should receive a (?P<expected_code>.+) response from (?P<container>.+)")
def step_impl(context, expected_code, container):
    """
    :type context: behave.runner.Context
    :type expected_code: str
    :type container: str
    """
    print(context.cmd.status_code)
    assert_equal(expected_code, str(context.cmd.status_code),
                 msg_fmt=f'Expected {expected_code} actual is {context.cmd.status_code}')


@when("the Endpoint http://(?P<ip_address>.+):(?P<port>.+)/(?P<endpoint>.+) is called")
def step_impl(context, ip_address, port, endpoint):
    """
    :type context: behave.runner.Context
    :type ip_address: str
    :type port: str
    :type endpoint: str
    """
    method = context.active_outline[3]
    body = context.active_outline[4]
    headers = context.active_outline[6]
    # headers = list(context.active_outline[6].split(","))
    print(f'method: {method}, IP: {ip_address}, port: {port}, endpoint: {endpoint}, body: {body}, headers: {headers}')
    url = f"http://{ip_address}:{port}/{endpoint}"
    context.cmd = request(method=method, url=url, body=body, headers=headers)
    print(context.cmd)
    print(context.cmd.text)
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')


@given("sdk-ip is set")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ip = context.active_outline[0]
    port = context.active_outline[1]
    endpoint = 'configuration/config/'
    method = 'GET'
    print(f'method: {method}, IP: {ip}, port: {port}, endpoint: {endpoint}')
    context.cmd = request(method, f'http://{ip}:{port}/{endpoint}', 'null')
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')
    # Add assertion here to check value of IP address(es)
    print(context.cmd.text)
    config_items = list(context.cmd.text.split(","))
    endpoints = config_items[13]
    assert_true(context.active_outline[7] in endpoints,
                msg_fmt=f'Expected sdk address {context.active_outline[7]}. Actual sdk address {endpoints}')


@step("the user has already run load files")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ip = context.active_outline[0]
    port = context.active_outline[1]
    endpoint = 'file-distributor/hd2/status'
    method = 'GET'
    print(f'method: {method}, IP: {ip}, port: {port}, endpoint: {endpoint}')
    context.cmd = request(method, f'http://{ip}:{port}/{endpoint}', 'null')
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')


@then("the user should receive a response showing the processing status")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    expected_code = context.active_outline[5]
    print(context.cmd.status_code)
    assert_equal(expected_code, str(context.cmd.status_code),
                 msg_fmt=f'Expected {expected_code} actual is {context.cmd.status_code}')
    print(context.cmd.text)


@then("the user should receive a (?P<expected_code>.+)")
def step_impl(context, expected_code):
    """
    :type context: behave.runner.Context
    :type expected_code: str
    """
    print(context.cmd.status_code)
    assert_equal(expected_code, str(context.cmd.status_code),
                 msg_fmt=f'Expected {expected_code} actual is {context.cmd.status_code}')


@step("showing the processing status")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.cmd.text)
    assert_true(context.active_outline[7] in context.cmd.text,
                msg_fmt=f'Expected Value {context.active_outline[7]} not found. Actual Value: {context.cmd.text}')


@step("the user should be able to see SDK IP set with provided IP list")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.cmd.text)
    assert_equal(context.active_outline[4].replace(" ", ""), str(context.cmd.text))


@step("the user should see a response showing the base directory matches the user input")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.cmd.text)
    assert_equal(context.active_outline[4].replace(" ", ""), str(context.cmd.text))


@step("the user will see response Confirming the files are loaded")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.cmd.text)
    assert_true(context.active_outline[8] in context.cmd.text,
                msg_fmt=f'Expected Value {context.active_outline[8]} not found. Actual Value: {context.cmd.text}')


@step('the user should be able to see the output confirming "Loop Completed"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    print(context.cmd.text)
    assert_true(context.active_outline[8] in context.cmd.text,
                msg_fmt=f'Expected Value {context.active_outline[8]} not found. Actual Value: {context.cmd.text}')


@step("the user can see the files show as copied in processing status")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ip = context.active_outline[0]
    port = context.active_outline[1]
    endpoint = 'processing/status'
    method = 'GET'
    print(f'method: {method}, IP: {ip}, port: {port}, endpoint: {endpoint}')
    context.cmd = request(method, f'http://{ip}:{port}/{endpoint}', 'null')
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')
    print(context.cmd.text)
    status_items = list(context.cmd.text.split(","))
    assert_equal(status_items[1].split(":")[1], status_items[2].split(":")[1],
                 msg_fmt=f'Expected: {status_items[1].split(":")[1]}, Actual: {status_items[2].split(":")[1]}')


@step("the user should see the HD3 with processed files")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    ip = context.active_outline[0]
    port = context.active_outline[1]
    endpoint = 'processing/status'
    method = 'GET'
    print(f'method: {method}, IP: {ip}, port: {port}, endpoint: {endpoint}')
    context.cmd = request(method, f'http://{ip}:{port}/{endpoint}', 'null')
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')
    print(context.cmd.text)
    status_items = list(context.cmd.text.split(","))
    assert_true(status_items[6].split(":")[1] == '0', msg_fmt=f'Expected files left to process 0. Actual {status_items[6].split(":")[1]}')


@step("the HD2 status is clear")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.cmd = request("POST", f'http://{context.ip}:{context.port}/pre-processor/clear-data-and-status', 'null')
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')