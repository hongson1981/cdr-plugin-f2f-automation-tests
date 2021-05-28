from behave import *
import subprocess


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
    context.cmd = os_cmd(f"curl -w {flag} http://localhost:{port}")
    print(context.cmd)
    # Verify response from endpoint
