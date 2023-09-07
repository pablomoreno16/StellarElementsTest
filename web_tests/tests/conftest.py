import os
import re
import shutil
import pytest
import pytest_html

evidences_dir = 'evidences'


@pytest.fixture(autouse=True, scope="session")
def setup_teardown():
    # delete evidences folder and create it again
    if os.path.isdir(evidences_dir):
        shutil.rmtree(evidences_dir, ignore_errors=True)
    if not os.path.isdir(evidences_dir):  # ask again in case the previous deletion failed
        os.mkdir(evidences_dir)
    yield


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call':
        # verify if test execution failed
        if report.failed:
            # get the driver
            driver = item.funcargs['browser']
            # take the screenshot and attach it to the test case
            method_name = item.name
            print('\ntest case {} failed.'.format(method_name))
            # save the screenshot in the directory
            method_name = re.sub(r'_|!|\s', '-', method_name)
            path_file = f"{evidences_dir}/{method_name}.png"
            driver.save_screenshot(path_file)
            # attach the screenshot to the html report
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(path_file))
            report.extras = extras
