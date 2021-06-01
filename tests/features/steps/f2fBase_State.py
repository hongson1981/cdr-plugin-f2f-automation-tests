from behave import *
import subprocess
from asserts import assert_true, assert_equal, assert_raises


def os_cmd(command):
    p = subprocess.check_output(command, shell=True)
    return p.decode("utf-8")


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
    Use a CURL command to send a request to http://localhost:<port>
    """
    flag = "'%{http_code}'"
    print(port)
    #context.cmd = os_cmd(f"curl -sw {flag} http://localhost:{port}")
    context.cmd = os_cmd(f"curl -I http://localhost:{port}")
    output = str(context.cmd)
    type(output)
    print(output)
    result = output.find("HTTP/1.1 200 OK")
    print(result)
    print(type(result))
    assert_true(result, msg_fmt=f'Expected {True} actual is {result}')
    # Verify response from endpoint


@then("the user should receive a (?P<expected_code>.+) response from (?P<container>.+)(?P<actual_code>.+)")
def step_impl(context, expected_code, container, actual_code):
    """
    :type context: behave.runner.Context
    :type expected_code: str
    :type container: str
    :type actual_code: str
    """
    output = str(context.cmd)
    type(output)
    print(output)
    result = output.find("HTTP/1.1 200 OK")
    print(result)
    print(type(result))
    assert_true(result, msg_fmt=f'Expected {True} actual is {result}')
