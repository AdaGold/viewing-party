import pytest
from viewing_party import main

def test_hw():
    assert main.hw()


def test_create_successful_movie():
    # Arrange
    movie_title = "Title A"
    genre = "Horror"
    rating = 3.5

    # Act
    new_movie = main.create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie["title"] is "Title A"

def test_create_no_title_movie():
    # Arrange
    movie_title = None
    genre = "Horror"
    rating = 3.5

    # Act
    new_movie = main.create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None

def test_create_no_genre_movie():
    # Arrange
    movie_title = "Title A"
    genre = None
    rating = 3.5

    # Act
    new_movie = main.create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None

def test_create_no_rating_movie():
    # Arrange
    movie_title = "Title A"
    genre = "Horror"
    rating = None

    # Act
    new_movie = main.create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None

def test_adds_movie_to_user_watched():
    # Arrange
    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    user_data = {
        "watched": []
    }

    # Act
    updated_data = main.add_to_watched(user_data, movie)

    # Assert
    assert len(updated_data["watched"]) is 1
    assert updated_data["watched"][0]["title"] is "Title A"
    assert updated_data["watched"][0]["genre"] is "Horror"
    assert updated_data["watched"][0]["rating"] is 3.5


def test_adds_movie_to_user_watchlist():
    # Arrange
    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }
    user_data = {
        "watchlist": []
    }

    # Act
    updated_data = main.add_to_watchlist(user_data, movie)

    # Assert
    assert len(updated_data["watchlist"]) is 1
    assert updated_data["watchlist"][0]["title"] is "Title A"
    assert updated_data["watchlist"][0]["genre"] is "Horror"
    assert updated_data["watchlist"][0]["rating"] is 3.5

def test_moves_movie_from_watchlist_to_empty_watched():
    # Arrange
    title = "Title A"
    janes_data = {
        "watchlist": [{
            "title": title,
            "genre": "Fantasy",
            "rating": 4.8
        }],
        "watched": []
    }

    # Act
    updated_data = main.watch_movie(janes_data, "Title A")

    # Assert
    assert len(updated_data["watchlist"]) is 0
    assert len(updated_data["watched"]) is 1
    assert updated_data["watched"][0]["title"] is "Title A"
    assert updated_data["watched"][0]["genre"] is "Fantasy"
    assert updated_data["watched"][0]["rating"] is 4.8


def test_moves_movie_from_watchlist_to_watched():
    # Arrange
    movie_to_watch = {
        "title": "Title A",
        "genre": "Fantasy",
        "rating": 4.8
    }
    janes_data = {
        "watchlist": [
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            },
            movie_to_watch
        ],
        "watched": [
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }

    # Act
    updated_data = main.watch_movie(janes_data, movie_to_watch["title"])

    # Assert
    assert len(updated_data["watchlist"]) is 1
    assert len(updated_data["watched"]) is 2
    assert movie_to_watch in updated_data["watched"]

def test_does_nothing_if_movie_not_in_watchlist():
    # Arrange
    movie_to_watch = {
        "title": "Title A",
        "genre": "Fantasy",
        "rating": 4.8
    }
    janes_data = {
        "watchlist": [
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            }
        ],
        "watched": [
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }

    # Act
    updated_data = main.watch_movie(janes_data, "Title A")

    # Assert
    assert len(updated_data["watchlist"]) is 1
    assert len(updated_data["watched"]) is 1
    assert movie_to_watch not in updated_data["watchlist"]
    assert movie_to_watch not in updated_data["watched"]

def test_calculates_watched_average_rating():
    # Arrange
    janes_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Fantasy",
                "rating": 4.8
            },
            {
                "title": "Title B",
                "genre": "Action",
                "rating": 2.0
            },
            {
                "title": "Title C",
                "genre": "Intrigue",
                "rating": 3.9
            }
        ]
    }

    # Act
    average = main.get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.56666666664)


def test_empty_watched_average_rating_is_zero():
    # Arrange
    janes_data = {
        "watched": [
        ]
    }

    # Act
    average = main.get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)

def test_most_watched_genre():
    # Arrange
    janes_data = {
        "watched": [
            {
                "title": "Title A",
                "genre": "Fantasy"
            },
            {
                "title": "Title B",
                "genre": "Intrigue"
            },
            {
                "title": "Title C",
                "genre": "Intrigue"
            },
            {
                "title": "Title D",
                "genre": "Fantasy"
            },
            {
                "title": "Title E",
                "genre": "Intrigue"
            },
        ]
    }

    # Act
    popular_genre = main.get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre is "Intrigue"

def test_genre_is_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = main.get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre is None

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
    amandas_unique_movies = main.get_unique_watched(amandas_data)

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
    amandas_unique_movies = main.get_unique_watched(amandas_data)

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
    friends_unique_movies = main.get_friends_unique_watched(amandas_data)

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
    friends_unique_movies = main.get_friends_unique_watched(amandas_data)

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
    friends_unique_movies = main.get_friends_unique_watched(amandas_data)

    # Arrange
    assert len(friends_unique_movies) is 0

def test_get_available_friend_rec():
    # Arrange
    amandas_data = {
        "subscriptions": [ "Service A", "Service B" ],
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
    recommendation = main.get_available_rec(amandas_data)

    # Arrange
    assert len(recommendation) is 2
    assert {"title": "Title A", "host": "Service A"} in recommendation
    assert {"title": "Title B", "host": "Service B"} in recommendation


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
    recommendation = main.get_available_rec(amandas_data)

    # Arrange
    assert len(recommendation) is 0
