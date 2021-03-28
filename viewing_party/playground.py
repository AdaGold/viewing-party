from main import get_new_rec_by_genre
from main import get_most_watched_genre
from main import get_friends_unique_watched
from main import unique_helper
# Arrange
user_data = {
    "watched": [
        {
            "title": "Title A",
            "genre": "Intrigue"
        },
        {
            "title": "Title B",
            "genre": "Intrigue"
        },
        {
            "title": "Title C",
            "genre": "Fantasy"
        }
    ],
    "friends": [
        {
            "watched": [
                {
                    "title": "Title D",
                    "genre": "Intrigue"
                }
            ]
        },
        {
            "watched": [
                {
                    "title": "Title C",
                    "genre": "Fantasy"
                },
                {
                    "title": "Title E",
                    "genre": "Intrigue"
                }
            ]
        }
    ]
}

get_new_rec_by_genre(user_data)
