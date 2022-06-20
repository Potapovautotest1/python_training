from fixture.Application import application
import pytest

fixture=None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture=application()
        fixture.session.login(username="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = application()
            fixture.session.login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture