import pytest
from viewing_party.main import *

### 3.1.1 PASSED ###
def test_get_unique_watched_returns_list_of_movies_in_amandas_data_absent_from_their_friends_data():
    # # Arrange - section of test that includes the things to arrange or set up.
    # (Arrange i.e.) Creating variables, calling helper methods - and setup needed to execute successfully.
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

    # Act - section of test that describes /determines WHAT NEEDS TO BE TESTED
    # (Act i.e.) if writing a unit test for a function, this is where we INVOKE the function.
    amandas_unique_movies = get_unique_watched(amandas_data)

    # Arrange?? -- this should be Assert
    # Assert  - section of test where any assert statements can be made (and tested)
    # Assert means - stating that something is true. The test will pass if this assert statement is True.
    assert len(amandas_unique_movies) is 2
    assert {"title": "Title B"} in amandas_unique_movies
    assert {"title": "Title E"} in amandas_unique_movies

### 3.1.2 PASSED ###
def test_get_unique_watched_returns_empty_list_when_amandas_movies_are_all_in_her_friends_movies():
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

    # Arrange?? -- this should be Assert
    # Assert  - section of test where any assert statements can be made (and tested)
    # Assert means - stating that something is true. The test will pass if this assert statement is True.
    assert len(amandas_unique_movies) is 0

### 3.2.1 PASSED ###
def test_get_friends_unique_watched_returns_list_of_movies_amanda_has_not_watched_and_friends_have_but_does_not_include_two_of_the_same_movie():
    # Arrange
    amandas_data = {
        "watched": [
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
    # should be assert?
    assert len(friends_unique_movies) is 3
    assert {"title": "Title A"} in friends_unique_movies
    assert {"title": "Title D"} in friends_unique_movies
    assert {"title": "Title E"} in friends_unique_movies

### 3.2.2 PASSED ###
def test_get_friends_unique_watched_returns_list_of_movies_amanda_has_not_watched_and_friends_have_with_only_one_friend():
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
    # should be assert?
    assert len(friends_unique_movies) is 3
    assert {"title": "Title A"} in friends_unique_movies
    assert {"title": "Title B"} in friends_unique_movies
    assert {"title": "Title C"} in friends_unique_movies

### 3.2.3 PASSED ###
def test_get_friends_unique_watched_returns_empty_list_when_amanda_has_seen_all_movies_their_friend_has_seen():
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

    # Arrange??
    # Arrange?? -- this should be Assert
    # Assert  - section of test where any assert statements can be made (and tested)
    # Assert means - stating that something is true. The test will pass if this assert statement is True.
    assert len(friends_unique_movies) is 0
