from pytest_bdd import scenario, given, when, then
import os


@given("that docker compose is up and running")
def test_docker_check():
    docker_out = str(os.system('docker ps'))
    assert docker_out.find('cdr_plugin_folder_to_folder')


# @when("the user runs docker ps")
# def test_docker_check():
#     docker_out = os.system('docker ps')
#     assert docker_out.find('cdr_plugin_folder_to_folder')


