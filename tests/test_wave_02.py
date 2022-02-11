import pytest
from viewing_party.party import *
import copy

@pytest.mark.skip()
def test_calculates_watched_average_rating():
    # Arrange
    janes_data = {
        'watched': [
            {
                'title': 'The Lord of the Functions: The Fellowship of the Function', 
                'genre': 'Fantasy', 
                'rating': 4.8
            }, 
            {
                'title': 'The Lord of the Functions: The Two Parameters', 
                'genre': 'Fantasy', 
                'rating': 4.0
            }, 
            {
                'title': 'The Lord of the Functions: The Return of the Value',
                'genre': 'Fantasy', 
                'rating': 4.0
            }, 
            {
                'title': 'The JavaScript and the React', 
                'genre': 'Action', 
                'rating': 2.2
            }, 
            {
                'title': 'Recursion', 
                'genre': 'Intrigue', 
                'rating': 2.0
            }, 
            {
                'title': 'Instructor Student TA Manager', 
                'genre': 'Intrigue', 
                'rating': 4.5
            }
        ]
    }

    janes_data_before = copy.deepcopy(janes_data)

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(3.58333)
    assert janes_data == janes_data_before

@pytest.mark.skip()
def test_empty_watched_average_rating_is_zero():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    average = get_watched_avg_rating(janes_data)

    # Assert
    assert average == pytest.approx(0.0)

@pytest.mark.skip()
def test_most_watched_genre():
    # Arrange
    janes_data = {
        'watched': [
            {
                'title': 'The Lord of the Functions: The Fellowship of the Function', 
                'genre': 'Fantasy', 
                'rating': 4.8
            }, 
            {
                'title': 'The Lord of the Functions: The Two Parameters', 
                'genre': 'Fantasy', 
                'rating': 4.0
            }, 
            {
                'title': 'The Lord of the Functions: The Return of the Value',
                'genre': 'Fantasy', 
                'rating': 4.0
            }, 
            {
                'title': 'The JavaScript and the React', 
                'genre': 'Action', 
                'rating': 2.2
            }, 
            {
                'title': 'Recursion', 
                'genre': 'Intrigue', 
                'rating': 2.0
            }, 
            {
                'title': 'Instructor Student TA Manager', 
                'genre': 'Intrigue', 
                'rating': 4.5
            }
        ]
    }
    janes_data_before = copy.deepcopy(janes_data)

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == "Fantasy"
    assert janes_data == janes_data_before

@pytest.mark.skip()
def test_genre_is_None_if_empty_watched():
    # Arrange
    janes_data = {
        "watched": []
    }

    # Act
    popular_genre = get_most_watched_genre(janes_data)

    # Assert
    assert popular_genre == None
