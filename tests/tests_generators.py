from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


def test_card_number_generator():
    assert list(card_number_generator(1, 1))[0] == '0000 0000 0000 0001'
    assert list(card_number_generator(56, 56))[0] == '0000 0000 0000 0056'
    assert list(card_number_generator(156, 157))[0] == '0000 0000 0000 0156', '0000 0000 0000 0157'
    assert list(card_number_generator(88888887, 88888888))[0] == '0000 0000 8888 8887', '0000 0000 8888 8888'


def test_transaction_descriptions(empty_list):
    assert list(transaction_descriptions(empty_list)) == []


def test_filter_by_currency(empty_list):
    assert list(filter_by_currency(empty_list, 'RUB')) == []
