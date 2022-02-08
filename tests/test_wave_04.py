import pytest
from viewing_party.party import *
from tests.test_constants import *


def test_get_available_friend_rec():
    # Arrange
    amandas_data = USER_DATA_4

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) is 2
    assert HORROR_1b in recommendations
    assert FANTASY_4b in recommendations
    assert amandas_data is USER_DATA_4


def test_no_available_friend_recs():
    # Arrange
    amandas_data = {
        "subscriptions": ["hulu", "disney+"],
        "watched": [],
        "friends": [
            {
                "watched": [HORROR_1b]
            },
            {
                "watched": [FANTASY_3b]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) is 0
