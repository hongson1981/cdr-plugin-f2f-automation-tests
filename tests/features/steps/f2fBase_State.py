from behave import *
from asserts import assert_true, assert_equal, assert_raises, assert_not_equal
import subprocess
import requests


def os_cmd(command):
    p = subprocess.check_output(command, shell=True)
    return p.decode("utf-8")


def request(method, url, body='null'):
    """
    :param method: Should be equal to 'GET' or 'POST'
    :param url: The url that will be called
    :param body: Should be supplied as this format { 'key1': 'value1', 'key2': 'value2' }
    :return: Will return the status call of the request, if an undefined method is passed, or a blank body supplied on
    a 'POST' request this function will return a string 'FAILED'. In your test step should assert that 'FAILED' was not
    returned.
    """
    if method == 'GET':
        get_request = requests.get(url)
        return get_request
    elif method == 'POST':
        if body == 'null':
            print('POST Requests expect a body, body parameter cannot be null')
            return 'FAILED'
        else:
            post_request = requests.post(url, data=body)
            return post_request
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
    # Verify contents of 'docker ps' output


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
    print(f'method: {method}, IP: {ip_address}, port: {port}, endpoint: {endpoint}, body: {body}')
    context.cmd = request(method, f'http://{ip_address}:{port}/{endpoint}', body)
    print(context.cmd)
    assert_not_equal('FAILED', str(context.cmd), msg_fmt='request method returned FAILED')


@step("sdk-ip is set")
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
    #Add assertion here to chack value of IP address(es)


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
    #assert response headers are as expected


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
    #Add assertion on response body
