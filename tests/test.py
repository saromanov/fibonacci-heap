import pytest
import fibonacci

def test_create_heap():
    f = fibonacci.FibonacciHeap()
    assert f.min() == None