import pytest

from mockalot.exceptions import InvalidParameterException
from mockalot.generators import PickFromListGenerator


def test_pick_from_list():
    elements = [i for i in range(5)]
    generator = PickFromListGenerator(elements=elements)
    picked_element = generator.generate()
    assert picked_element in elements


def test_validate_fail_empty_elements():
    elements = list()
    with pytest.raises(InvalidParameterException):
        PickFromListGenerator(elements=elements)

def test_validate_fail_single_element():
    elements = ["a"]
    with pytest.raises(InvalidParameterException):
        PickFromListGenerator(elements=elements)
