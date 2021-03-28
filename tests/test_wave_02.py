import pytest
from viewing_party.main import *

### 2.1.1 PASSED ###

def test_get_watched_avg_rating_calculates_watched_average_rating():
    # Arrange - section of test that includes the things to arrange or set up.
    # (Arrange i.e.) Creating variables, calling helper methods - and setup needed to execute successfully.
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

    # Act - section of test that describes /determines WHAT NEEDS TO BE TESTED
    # (Act i.e.) if writing a unit test for a function, this is where we INVOKE the function.
    average = get_watched_avg_rating(janes_data)

    # Assert  - section of test where any assert statements can be made (and tested)
    # Assert means - stating that something is true. The test will pass if this assert statement is True.
    assert average == pytest.approx(3.56666666664)

### 2.1.2 PASSED ###

def test_get_watched_avg_rating_returns_zero_for_empty_list():
    # Arrange
    janes_data = {
        "watched": [
        ]
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)

### 2.2.1 ###

def test_get_most_watched_genre_returns_most_frequent_genre_from_list():
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
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre is "Intrigue"

### 2.2.2 SOLVED ###

def test_get_most_watched_genre_returns_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre is None
