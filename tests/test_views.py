from app.views import *

def test_index():
    assert index() == 'Hello World!', 'Index value incorrect'
