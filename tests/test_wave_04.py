import pytest
from viewing_party.main import create_movie, add_to_watched, add_to_watchlist, watch_movie, get_watched_avg_rating, get_most_watched_genre, get_unique_watched, get_friends_unique_watched, get_available_recs


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


