import pytest
from viewing_party.main import *


def test_get_available_friend_rec():
    # Arrange
    amandas_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "host": "Service A"
                    },
                    {
                        "title": "Title C",
                        "host": "Service C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A",
                        "host": "Service A"
                    },
                    {
                        "title": "Title B",
                        "host": "Service B"
                    },
                    {
                        "title": "Title D",
                        "host": "Service D"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) is 2
    assert {"title": "Title A", "host": "Service A"} in recommendations
    assert {"title": "Title B", "host": "Service B"} in recommendations


def test_no_available_friend_recs():
    # Arrange
    amandas_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title C",
                        "host": "Service C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title D",
                        "host": "Service D"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_available_recs(amandas_data)

    # Arrange
    assert len(recommendations) is 0
