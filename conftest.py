
from fixture.Application import application
import pytest



@pytest.fixture(scope = "session")
def app(request):
    fixture=application()
    request.addfinalizer(fixture.destroy)
    return fixture