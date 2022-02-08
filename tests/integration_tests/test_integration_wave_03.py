import pytest
from viewing_party.party import *
from tests.test_constants import *

@pytest.mark.integration_test
def test_get_friends_unique():
    user_data = USER_DATA_3

    unique_movies = get_unique_watched(user_data)

    assert FANTASY_2 in unique_movies
    assert INTRIGUE_2 in unique_movies
    assert len(unique_movies) == 2

    friend_unique_movies = get_friends_unique_watched(user_data)

    assert len(friend_unique_movies) == 3
    assert INTRIGUE_3 in friend_unique_movies
    assert HORROR_1 in friend_unique_movies
    assert FANTASY_4 in friend_unique_movies