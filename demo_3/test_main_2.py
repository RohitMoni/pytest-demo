import pytest

@pytest.fixture(scope="module")
def shared_instance():
    instance = {
        'enabled': True
    }
    yield instance
    print("teardown instance")
    instance['enabled'] = False

def test_enabled(shared_instance):
    assert(shared_instance['enabled'])