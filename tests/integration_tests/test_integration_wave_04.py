import pytest
from viewing_party.party import *
from tests.test_constants import *

@pytest.mark.integration_test
def test_get_available_recs():
    #Arrange
    user_data = USER_DATA

    rec_movies = get_available_recs(user_data)

    assert len(rec_movies) == 2
    assert HORROR_1 in rec_movies
    assert FANTASY_4 in rec_movies