import pytest
from flask import json

from app import app
from itertools import combinations


@pytest.fixture(scope="module")
def test_client():
    app.testing = True
    return app.test_client()


def test_missing_argument_causes_400(test_client):
    assert all(
        test_client.post('/estimate', data=dict(args)).status_code == 400
        for args in combinations([('my_hand', "S6,CK"), ('opponent_count', 3), ('table', "HK,HA,HT")], 2))


def test_valid_request_succeeds(test_client):
    result = test_client.post('/estimate', data={'my_hand': "HA,CK", "table": "", "opponent_count": 3})
    assert result.status_code == 200
    assert result.content_type == 'application/json'
    data_dict = json.loads(result.data)
    assert 'probability' in data_dict
    assert 1.0 > data_dict['probability'] > 0.0


def test_invalid_arguments_cause_400(test_client):
    cases = [
        # invalid number of cards in my hand
        {'my_hand': "HA", "table": "", "opponent_count": 3},
        # invalid number of cards on the table
        {'my_hand': "HA,CK", "table": "CT", "opponent_count": 3},
        # invalid number of opponents
        {'my_hand': "HA,CK", "table": "", "opponent_count": 0},
        # invalid card in hand
        {'my_hand': "HAZ,CK", "table": "", "opponent_count": 3},
        # invalid card on the table
        {'my_hand': "HA,CK", "table": "HT,CT,CY", "opponent_count": 3}]

    assert all(test_client.post('/estimate', data=dict(args)).status_code == 400 for args in cases)