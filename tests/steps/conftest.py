import pytest
from pytest_bdd import scenario, given, when, then


# Constants


# Hooks


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')


# Fixtures

# @pytest.fixture
# def browser():
#     # For this example, we will use Firefox
#     # You can change this fixture to use other browsers, too.
#     # A better practice would be to get browser choice from a config file.
#     b = webdriver.Firefox()
#     b.implicitly_wait(10)
#     yield b
#     b.quit()


# Shared Given Steps

# @given("that docker compose is up and running")
# def test_docker_check():
#     docker_out = str(os.system('docker ps'))
#     assert docker_out.find('cdr_plugin_folder_to_folder')
