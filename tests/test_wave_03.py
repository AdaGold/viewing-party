import pytest
from viewing_party.main import *


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
