#----------WAVE01-------------
MOVIE_TITLE_1 = "It came from the stack trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

#----------WAVE02-------------
HORROR_1 = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
}

FANTASY_1 = {
    "title": "Fantasy 1",
    "genre": "Fantasy",
    "rating": 4.8
}

FANTASY_2 = {
    "title": "Fantasy 2",
    "genre": "Fantasy",
    "rating": 4.0
}

FANTASY_3 = {
    "title": "Fantasy 3",
    "genre": "Fantasy",
    "rating": 4.0
}

FANTASY_4 = {
    "title": "Fantasy 4",
    "genre": "Fantasy",
    "rating": 4.0
}

ACTION_1 = {
    "title": "Action 1",
    "genre": "Action",
    "rating": 2.2
}

ACTION_2 = {
    "title": "Action 2",
    "genre": "Action",
    "rating": 4.2
}

ACTION_3 = {
    "title": "Action 3",
    "genre": "Action",
    "rating": 3.5
}

INTRIGUE_1 = {
    "title": "Intrigue 1",
    "genre": "Intrigue",
    "rating": 2.0
}

INTRIGUE_2 = {
    "title": "Intrigue 2",
    "genre": "Intrigue",
    "rating": 4.5
}

INTRIGUE_3 = {
    "title": "Intrigue 3",
    "genre": "Intrigue",
    "rating": 3.0
}
USER_DATA = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],    
}

EMPTY_USER_DATA = {
    "watched": [],
}

#-----WAVE 3--------
USER_DATA["friends"] =  [
        {
            "watched": [
                FANTASY_1,
                FANTASY_3,
                FANTASY_4,
                HORROR_1,
            ]
        },
        {
            "watched": [
                FANTASY_1,
                ACTION_1,
                INTRIGUE_1,
                INTRIGUE_3,
            ]
        }
    ]  

#-----WAVE 4--------
HORROR_1["host"] = "netflix"
FANTASY_1["host"] = "netflix"
FANTASY_2["host"] = "netflix"
FANTASY_3["host"] = "amazon"
FANTASY_4["host"] = "hulu"
ACTION_1["host"] = "amazon"
ACTION_2["host"] = "amazon"
ACTION_3["host"] = "hulu"
INTRIGUE_1["host"] = "hulu"
INTRIGUE_2["host"] = "disney+"
INTRIGUE_3["host"] = "disney+"

USER_DATA["subscriptions"] = ["netflix", "hulu"]  


#----WAVE 5-----------

USER_DATA["favorites"] = [
    FANTASY_1, 
    FANTASY_2, 
    INTRIGUE_1,
    INTRIGUE_2
    ]