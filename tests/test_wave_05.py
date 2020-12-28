import pytest
from viewing_party.main import *


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
