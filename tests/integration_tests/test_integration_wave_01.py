import pytest
from viewing_party.party import *
from tests.test_constants import *

@pytest.mark.integration_test
def test_create_and_watch_movie():
    # Arrange
    movie_title = MOVIE_TITLE_1
    genre = GENRE_1
    rating = RATING_1
    user_data = {"watched": [], "watchlist": []}

    # Act
    # create movie
    new_movie = create_movie(movie_title, genre, rating)

    # add movie to watchlist
    add_to_watchlist(user_data, new_movie)

    # check that the movie is the first item in the watch list
    assert user_data["watchlist"][0]["title"] == MOVIE_TITLE_1
    assert user_data["watchlist"][0]["genre"] == GENRE_1
    assert user_data["watchlist"][0]["rating"] == RATING_1

    # watch movie
    watch_movie(user_data, movie_title)

    #check that watch list is empty and new movie is in watched
    assert user_data["watchlist"] == []
    assert user_data["watched"][0]["title"] == MOVIE_TITLE_1
    assert user_data["watched"][0]["genre"] == GENRE_1
    assert user_data["watched"][0]["rating"] == RATING_1

    # try to watch movie not in watchlist
    watch_movie(user_data, movie_title)

    # confirm there is still only 1 movie in watched
    assert len(user_data["watched"]) == 1



