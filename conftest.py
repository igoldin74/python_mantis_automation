import pytest
import json
import jsonpickle
import os.path
from fixture.application import Application
import importlib
from fixture.db import DbFixture


fixture = None
target = None

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture
def app(request, config):
    global fixture
    global target
    browser = request.config.getoption('--browser')
    if fixture is None or fixture.is_not_valid():
        fixture = Application(browser=browser, config=config)
    return fixture


@pytest.fixture(scope="session", autouse=True)
def db(request):
    db_config = load_config(request.config.getoption("--target"))["DB"]
    dbfixture = DbFixture(host=db_config["host"], database=db_config["name"], user=db_config["user"],
                          password=db_config["password"])

    def fin():
        dbfixture.destroy()
        request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='firefox')
    parser.addoption('--target', action='store', default='target.json')


# very little idea of how this block works:
def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(module):
    return importlib.import_module("data.%s" % module).test_data


def load_from_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target



