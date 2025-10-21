from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator
import pytest


@pytest.mark.parametrize('x, y, expected', [(1, 1, '0000 0000 0000 0001'), (56, 56, '0000 0000 0000 0056'),
                                            (4444, 4444, '0000 0000 0000 4444'),
                                            (12345678, 12345678, '0000 0000 1234 5678')])
def test_card_number_generator(x, y, expected):
    assert list(card_number_generator(x, y))[0] == expected
    assert list(card_number_generator(156, 157))[0] == '0000 0000 0000 0156', '0000 0000 0000 0157'
    assert list(card_number_generator(88888887, 88888888))[0] == '0000 0000 8888 8887', '0000 0000 8888 8888'
    assert list(card_number_generator(333344445555, 333344445556))[0] == '0000 3333 4444 5555', '0000 3333 4444 5556'


def test_transaction_descriptions(empty_list):
    assert list(transaction_descriptions(empty_list)) == []


def test_filter_by_currency(empty_list):
    assert list(filter_by_currency(empty_list, 'RUB')) == []
