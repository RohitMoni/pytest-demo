import pytest


@pytest.fixture
def bell_data():
    return {
        'name': 'Bell',
        'license': 'packet-broker',
        'expiration': 'infinite'
    }