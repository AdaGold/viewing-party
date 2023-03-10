import copy

# ********************************
# *** Do Not Modify This File ****
# ********************************

# Data for Unit Tests

#----------WAVE01-------------
MOVIE_TITLE_1 = "It Came from the Stack Trace"
GENRE_1 = "Horror"
RATING_1 = 3.5

#----------WAVE02-------------
HORROR_1 = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
}
FANTASY_1 = {
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
}
FANTASY_2 = {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_3 = {
    "title": "The Lord of the Functions: The Return of the Value",
    "genre": "Fantasy",
    "rating": 4.0
}
FANTASY_4 = {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
}
ACTION_1 = {
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
}
ACTION_2 = {
    "title": "2 JavaScript 2 React",
    "genre": "Action",
    "rating": 4.2
}
ACTION_3 = {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5
}
INTRIGUE_1 = {
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
}
INTRIGUE_2 = {
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}
INTRIGUE_3 = {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}
USER_DATA_2 = {
    "watched": [
        FANTASY_1, 
        FANTASY_2, 
        FANTASY_3, 
        ACTION_1, 
        INTRIGUE_1, 
        INTRIGUE_2
        ],    
}

USER_DATA_2b = {
    "watched": [
        INTRIGUE_1,
        FANTASY_2,
        ACTION_1,
        FANTASY_1,
        FANTASY_3,
        INTRIGUE_2,
    ]
}

#-----WAVE 3--------
USER_DATA_3 = copy.deepcopy(USER_DATA_2)
USER_DATA_3["friends"] =  [
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

HORROR_1b = copy.deepcopy(HORROR_1)
FANTASY_1b = copy.deepcopy(FANTASY_1)
FANTASY_2b = copy.deepcopy(FANTASY_2)
FANTASY_3b = copy.deepcopy(FANTASY_3)
FANTASY_4b = copy.deepcopy(FANTASY_4)
ACTION_1b = copy.deepcopy(ACTION_1)
ACTION_2b = copy.deepcopy(ACTION_2)
ACTION_3b = copy.deepcopy(ACTION_3)
INTRIGUE_1b = copy.deepcopy(INTRIGUE_1)
INTRIGUE_2b = copy.deepcopy(INTRIGUE_2)
INTRIGUE_3b = copy.deepcopy(INTRIGUE_3)

HORROR_1b["host"] = "netflix"
FANTASY_1b["host"] = "netflix"
FANTASY_2b["host"] = "netflix"
FANTASY_3b["host"] = "amazon"
FANTASY_4b["host"] = "hulu"
ACTION_1b["host"] = "amazon"
ACTION_2b["host"] = "amazon"
ACTION_3b["host"] = "hulu"
INTRIGUE_1b["host"] = "hulu"
INTRIGUE_2b["host"] = "disney+"
INTRIGUE_3b["host"] = "disney+"

USER_DATA_4 = {
    "watched": [
        FANTASY_1b, 
        FANTASY_2b, 
        FANTASY_3b, 
        ACTION_1b, 
        INTRIGUE_1b, 
        INTRIGUE_2b
        ],  
    "friends":  [
        {
            "watched": [
                FANTASY_1b,
                FANTASY_3b,
                FANTASY_4b,
                HORROR_1b,
            ]
        },
        {
            "watched": [
                FANTASY_1b,
                FANTASY_4b,
                ACTION_1b,
                INTRIGUE_1b,
                INTRIGUE_3b,
            ]
        }  
    ]
}

USER_DATA_4["subscriptions"] = ["netflix", "hulu"]  


#----WAVE 5-----------

USER_DATA_5 = copy.deepcopy(USER_DATA_4)

USER_DATA_5["favorites"] = [
    FANTASY_1b, 
    FANTASY_2b, 
    INTRIGUE_1b,
    INTRIGUE_2b
    ]

#----Functions that return clean data for each test----

def clean_wave_2_data():
    return copy.deepcopy(USER_DATA_2)

def clean_wave_2b_data():
    return copy.deepcopy(USER_DATA_2b)

def clean_wave_3_data():
    return copy.deepcopy(USER_DATA_3)

def clean_wave_4_data():
    return copy.deepcopy(USER_DATA_4)

def clean_wave_5_data():
    return copy.deepcopy(USER_DATA_5)