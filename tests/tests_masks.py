from src.masks import get_mask_card_number
from src.masks import get_mask_account

"""Тесты для номера карты"""


def test_get_mask_card_number(empty_list):
    assert get_mask_card_number('7000792289606361') == '7000 79** **** 6361'
    assert get_mask_card_number('123456789012') == '1234 56** ****'
    assert get_mask_card_number('700079228960636112345678') == '7000 79** **** 6361 1234 5678'
    assert get_mask_account('1') == ''
    assert get_mask_account(empty_list) == ''


"""Тесты для номера счета"""


def test_get_mask_account(empty_list):
    assert get_mask_account('73654108430135874305') == '**4305'
    assert get_mask_account('1234567890') == '**7890'
    assert get_mask_account('1234567890123456789012345') == '**2345'
    assert get_mask_account('1') == ''
    assert get_mask_account(empty_list) == ''
