import pytest
from viewing_party.party import *
from tests.test_constants import *

@pytest.mark.integration_test
def test_get_most_watched_genre():
    # Arrange
    user_data = USER_DATA
    empty_user_data = EMPTY_USER_DATA

    # user data
    most_watched = get_most_watched_genre(user_data)
    average_rating = get_watched_avg_rating(user_data)
    assert most_watched == "Fantasy"
    assert average_rating == pytest.approx(3.58333)

    # empty user data
    most_watched = get_most_watched_genre(empty_user_data)
    average_rating = get_watched_avg_rating(empty_user_data)
    assert most_watched == None
    assert average_rating == 0

    
    