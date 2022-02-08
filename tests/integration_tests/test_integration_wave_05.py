from cmath import rect
import pytest
from viewing_party.party import *
from tests.test_constants import *

@pytest.mark.integration_test
def test_recs():
    user_data = USER_DATA_5

    genre_rec = get_new_rec_by_genre(user_data)

    assert len(genre_rec) == 1
    assert FANTASY_4b in genre_rec

    favorite_recs = get_rec_from_favorites(user_data)

    assert len(favorite_recs) == 2
    assert FANTASY_2b in favorite_recs
    assert INTRIGUE_2b in favorite_recs