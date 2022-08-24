import pytest
from demo.app import create_app
from config import settings


@pytest.fixture(scope="session")
def app():
    """
    Setup our flask test app, this only gets executed once.

    :return: Flask app
    """
    params = {"SERVER_NAME": settings.SERVER_NAME}

    _app = create_app(params)

    # Establish an application context before running the tests.

    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="function")
def client(app):
    """
    Setup an app client, this gets executed for each test function.

    :param app: Pytest fixture
    :return: Flask app client
    """
    yield app.test_client()
