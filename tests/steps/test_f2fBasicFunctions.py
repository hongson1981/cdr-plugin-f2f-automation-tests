import pytest
from pytest_bdd import scenario, given, when, then
import pdb
import os
import subprocess


def system_out(command):
    p = subprocess.check_output(command, shell=True)
    return p.decode("utf-8")


@given("that docker compose is up and running")
def test_docker_check():
    out = system_out('docker ps')
    # docker_out = str(os.system('docker ps'))
    pdb.set_trace()
    assert out.find('')

# @when("the user runs docker ps")
# def test_docker_check():
#     docker_out = os.system('docker ps')
#     assert docker_out.find('cdr_plugin_folder_to_folder')
