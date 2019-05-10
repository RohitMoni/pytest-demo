import pytest

def increment(x):
    return x + 1

def trim(x):
    return x.strip()

# ------------------------------------------

@pytest.fixture
def shared_data():
    return {
        'someKey': ' someValue ',
        'someOtherKey': 52
    }

def test_increment(shared_data):
    assert(increment(shared_data['someOtherKey']) == 53)

def test_trim(shared_data):
    assert(trim(shared_data['someKey']) == 'someValue')