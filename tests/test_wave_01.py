import pytest
# NOTE: In production code, we developers should change import * to something more specific. Due to some constraints of this project, we will import * in our test files.
# from viewing_party.main import *
from viewing_party.party import *
from tests.test_constants import *

@pytest.mark.skip()
def test_create_successful_movie():
    # Arrange
    movie_title = MOVIE_TITLE_1
    genre = GENRE_1
    rating = RATING_1

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie["title"] == MOVIE_TITLE_1
    assert new_movie["genre"] == GENRE_1
    assert new_movie["rating"] == pytest.approx(RATING_1)

@pytest.mark.skip()
def test_create_no_title_movie():
    # Arrange
    movie_title = None
    genre = "Horror"
    rating = 3.5

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None

@pytest.mark.skip()
def test_create_no_genre_movie():
    # Arrange
    movie_title = "Title A"
    genre = None
    rating = 3.5

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None

@pytest.mark.skip()
def test_create_no_rating_movie():
    # Arrange
    movie_title = "Title A"
    genre = "Horror"
    rating = None

    # Act
    new_movie = create_movie(movie_title, genre, rating)

    # Assert
    assert new_movie is None

@pytest.mark.skip()
def test_adds_movie_to_user_watched():
    # Arrange
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
    user_data = {
        "watched": []
    }

    # Act
    updated_data = add_to_watched(user_data, movie)

    # Assert
    assert len(updated_data["watched"]) == 1
    assert updated_data["watched"][0]["title"] == MOVIE_TITLE_1
    assert updated_data["watched"][0]["genre"] == GENRE_1
    assert updated_data["watched"][0]["rating"] == RATING_1

@pytest.mark.skip()
def test_adds_movie_to_non_empty_user_watched():
    # Arrange
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
    user_data = {
        "watched": [FANTASY_2]
    }

    # Act
    updated_data = add_to_watched(user_data, movie)

    # Assert
    assert len(updated_data["watched"]) == 2
    assert movie in updated_data["watched"]
    assert FANTASY_2 in updated_data["watched"]

@pytest.mark.skip()
def test_adds_movie_to_user_watchlist():
    # Arrange
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
    user_data = {
        "watchlist": []
    }

    # Act
    updated_data = add_to_watchlist(user_data, movie)

    # Assert
    assert len(updated_data["watchlist"]) == 1
    assert updated_data["watchlist"][0]["title"] == MOVIE_TITLE_1
    assert updated_data["watchlist"][0]["genre"] == GENRE_1
    assert updated_data["watchlist"][0]["rating"] == RATING_1

@pytest.mark.skip()
def test_adds_movie_to_non_empty_user_watchlist():
    # Arrange
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
    user_data = {
        "watchlist": [FANTASY_2]
    }

    # Act
    updated_data = add_to_watchlist(user_data, movie)

    # Assert
    assert len(updated_data["watchlist"]) == 2
    assert movie in updated_data["watchlist"]
    assert FANTASY_2 in updated_data["watchlist"]

@pytest.mark.skip()
def test_moves_movie_from_watchlist_to_empty_watched():
    # Arrange
    janes_data = {
        "watchlist": [{
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }],
        "watched": []
    }

    # Act
    updated_data = watch_movie(janes_data, MOVIE_TITLE_1)

    # Assert
    assert len(updated_data["watchlist"]) == 0
    assert len(updated_data["watched"]) == 1
    
    raise Exception("Test needs to be completed.")
    # *******************************************************************************************
    # ****** Add assertions here to test that the correct movie was added to "watched" **********
    # *******************************************************************************************

@pytest.mark.skip()
def test_moves_movie_from_watchlist_to_watched():
    # Arrange
    movie_to_watch = HORROR_1
    janes_data = {
        "watchlist": [
            FANTASY_1,
            movie_to_watch
        ],
        "watched": [FANTASY_2]
    }

    # Act
    updated_data = watch_movie(janes_data, movie_to_watch["title"])

    # Assert
    assert len(updated_data["watchlist"]) == 1
    assert len(updated_data["watched"]) == 2
    
    raise Exception("Test needs to be completed.")
    # *******************************************************************************************
    # ****** Add assertions here to test that the correct movie was added to "watched" **********
    # *******************************************************************************************

@pytest.mark.skip()
def test_does_nothing_if_movie_not_in_watchlist():
    # Arrange
    movie_to_watch = HORROR_1
    janes_data = {
        "watchlist": [FANTASY_1],
        "watched": [FANTASY_2]
    }

    # Act
    updated_data = watch_movie(janes_data, "Non-Existent Movie Title")

    # Assert
    assert len(updated_data["watchlist"]) == 1
    assert len(updated_data["watched"]) == 1
    assert movie_to_watch not in updated_data["watchlist"]
    assert movie_to_watch not in updated_data["watched"]
