from behave import *
from asserts import assert_true, assert_equal, assert_raises
import subprocess
import requests


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
    context.cmd = requests.get(f"http://localhost:{port}")
    print(context.cmd.status_code)


@then("the user should receive a (?P<expected_code>.+) response from (?P<container>.+)")
def step_impl(context, expected_code, container):
    """
    :type context: behave.runner.Context
    :type expected_code: str
    :type container: str
    """
    assert_equal(int(expected_code), context.cmd.status_code, msg_fmt=f'Expected {expected_code} actual is {context.cmd.status_code}')
