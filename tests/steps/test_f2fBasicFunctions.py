#import pytest
#from behave import scenario, given, when, then
from behave import *
import os
import subprocess

def system_out(command):
    p = subprocess.check_output(command, shell=True)
    return p.decode("utf-8")


#@given("that docker compose is up and running")
#def test_docker_check():
#    out = system_out('docker ps')
#    assert out.find('abuntu')

# @when("the user runs docker ps")
# def test_docker_check():
#     docker_out = os.system('docker ps')
#     assert docker_out.find('cdr_plugin_folder_to_folder')