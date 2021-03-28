import pytest
from viewing_party.main import *


def test_get_available_recs_returns_appropriate_recommendations_for_valid_input():
    # # Arrange - section of test that includes the things to arrange or set up.
    # (Arrange i.e.) Creating variables, calling helper methods - and setup needed to execute successfully.
    amandas_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title A",
                        "host": "Service A"
                    },
                    {
                        "title": "Title C",
                        "host": "Service C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title A",
                        "host": "Service A"
                    },
                    {
                        "title": "Title B",
                        "host": "Service B"
                    },
                    {
                        "title": "Title D",
                        "host": "Service D"
                    }
                ]
            }
        ]
    }

    # Act - section of test that describes /determines WHAT NEEDS TO BE TESTED
    # (Act i.e.) if writing a unit test for a function, this is where we INVOKE the function.
    recommendations = get_available_recs(amandas_data)

    # Arrange?? - or assert?
    # Assert  - section of test where any assert statements can be made (and tested)
    # Assert means - stating that something is true. The test will pass if this assert statement is True.
    assert len(recommendations) is 2
    assert {"title": "Title A", "host": "Service A"} in recommendations
    assert {"title": "Title B", "host": "Service B"} in recommendations


def test_get_available_recs_returns_empty_list_for_valid_input_with_no_intersection_in_subscriptions():
    # Arrange
    amandas_data = {
        "subscriptions": ["Service A", "Service B"],
        "watched": [],
        "friends": [
            {
                "watched": [
                    {
                        "title": "Title C",
                        "host": "Service C"
                    }
                ]
            },
            {
                "watched": [
                    {
                        "title": "Title D",
                        "host": "Service D"
                    }
                ]
            }
        ]
    }

    # Act - section of test that describes /determines WHAT NEEDS TO BE TESTED
    # (Act i.e.) if writing a unit test for a function, this is where we INVOKE the function.
    recommendations = get_available_recs(amandas_data)

    # Arrange?? - should be Assert
    # Assert  - section of test where any assert statements can be made (and tested)
    # Assert means - stating that something is true. The test will pass if this assert statement is True.
    assert len(recommendations) is 0
