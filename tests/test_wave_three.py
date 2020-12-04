import pytest
from viewing_party.main import create_movie, add_to_watched, add_to_watchlist, watch_movie, get_watched_avg_rating, get_most_watched_genre, get_unique_watched, get_friends_unique_watched, get_available_recs, get_new_rec_by_genre, get_rec_from_favorites

def test_my_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            },
            {
                "title": "Title D"
            },
            {
                "title": "Title E"
            },
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title D"
                    },
                    {
                        "title": "Title F"
                    }
                ]
            }
        ]
    }

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Arrange
    assert len(amandas_unique_movies) is 2
    assert {"title": "Title B"} in amandas_unique_movies
    assert {"title": "Title E"} in amandas_unique_movies


def test_my_not_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title D"
                    },
                    {
                        "title": "Title F"
                    }
                ]
            }
        ]
    }

    # Act
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Arrange
    assert len(amandas_unique_movies) is 0


def test_friends_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title D"
                    },
                    {
                        "title": "Title E"
                    }
                ]
            }
        ]
    }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) is 2
    assert {"title": "Title D"} in friends_unique_movies
    assert {"title": "Title E"} in friends_unique_movies


def test_friends_unique_movies_not_duplicated():
    # Arrange
    amandas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title B"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            }
        ]
    }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) is 3
    assert {"title": "Title A"} in friends_unique_movies
    assert {"title": "Title B"} in friends_unique_movies
    assert {"title": "Title C"} in friends_unique_movies


def test_friends_not_unique_movies():
    # Arrange
    amandas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A"
                    },
                    {
                        "title": "Title C"
                    }
                ]
            },
            {
                "watched": []
            }
        ]
    }

    # Act
    friends_unique_movies = get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) is 0


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


def test_new_genre_rec():
    # Arrange
    sonyas_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Intrigue"
            },
            {
                "title": "Title B",
                "genre": "Intrigue"
            },
            {
                "title": "Title C",
                "genre": "Fantasy"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title D",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title C",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title E",
                        "genre": "Intrigue"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_new_rec_by_genre(sonyas_data)

    # Assert
    for rec in recommendations:
        assert rec not in sonyas_data["watched"]
    assert len(recommendations) is 2
    assert {"title": "Title D", "genre": "Intrigue"} in recommendations
    assert {"title": "Title E", "genre": "Intrigue"} in recommendations


def test_new_genre_rec_from_empty_watched():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title B",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title C",
                        "genre": "Intrigue"
                    }
                ]
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
        "watched": [
            {
                "title": "Title A",
                "genre": "Intrigue"
            }
        ],
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
    sonyas_data = {
        "watched": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            },
            {
                "title": "Title C"
            }
        ],
        "favorites": [
            {
                "title": "Title A"
            },
            {
                "title": "Title B"
            }
        ],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title B"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title C"
                    },
                    {
                        "title": "Title D"
                    }
                ]
            }
        ]
    }

    # Act
    recommendations = get_rec_from_favorites(sonyas_data)

    # Assert
    assert len(recommendations) is 1
    assert {"title": "Title A"} in recommendations


def test_unique_from_empty_favorites():
    # Arrange
    sonyas_data = {
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "genre": "Intrigue"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title B",
                        "genre": "Fantasy"
                    },
                    {
                        "title": "Title C",
                        "genre": "Intrigue"
                    }
                ]
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
        "watched": [
            {
                "title": "Title A",
                "genre": "Intrigue"
            }
        ],
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
