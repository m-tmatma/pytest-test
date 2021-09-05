import pytest

def pytest_addoption(parser):
	parser.addoption('--target', action='store', default='hogehoge', help='target')

@pytest.fixture
def target(request):
	'''specify target IP Address'''
	return request.config.getoption('--target')
