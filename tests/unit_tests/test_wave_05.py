import pytest
from viewing_party.party import *
from tests.test_constants import *


def test_new_genre_rec():
    # Arrange
    sonyas_data = USER_DATA_5

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    for rec in recommendations:
        assert rec not in sonyas_data["watched"]
    assert len(recommendations) is 1
    assert FANTASY_4b in recommendations


def test_new_genre_rec_from_empty_watched():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [INTRIGUE_1b]
            },
            {
                "watched": [INTRIGUE_2b,HORROR_1b]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0


def test_new_genre_rec_from_empty_friends():
    # Arrange
    sonyas_data = {
        "watched": [INTRIGUE_1b],
        "friends": [
            {
                "watched": []
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0


def test_unique_rec_from_favorites():
    # Arrange
    sonyas_data = USER_DATA_5

    # Act
    recommendations = get_rec_from_favorites(sonyas_data)

    # Assert
    assert len(recommendations) is 2
    assert FANTASY_2b in recommendations
    assert INTRIGUE_2b in recommendations


def test_unique_from_empty_favorites():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [INTRIGUE_1b]
            },
            {
                "watched": [INTRIGUE_2b,HORROR_1b]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0


def test_new_rec_from_empty_friends():
    # Arrange
    sonyas_data = {
        "watched": [INTRIGUE_1b],
        "friends": [
            {
                "watched": []
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    assert len(recommendations) is 0
