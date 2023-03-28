# ------------- WAVE 1 --------------------

"""
    first function create movie
    function takes 3 paramaters/attributes, titles, genre, rating
    if three attributers are truthy, return dictionary
    if title falsy, genre is falsy or rating is falsy, these should return none
    
"""
# 1st function
def create_movie(title, genre, rating):
    
    #possible us of isinstance method

    if title is None or genre is None or rating is None:
        return None

    new_movie = {"title": title, "genre": genre, "rating": rating}

    if isinstance(title, str) or isinstance(genre, str) or isinstance(rating, int):
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    else:
        return None

    return new_movie

# 2nd function
def add_to_watched(user_data, movie):

    (user_data["watched"]).append(movie)
    return user_data
    if not movie:
        user_data["watched"].append(movie)

#3rd function
def add_to_watchlist(user_data, movie):

    watchlist = user_data.get("watchlist", [])

    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    
    return user_data


# watch_movie testing info, please leave commented incase it breaks
# user_data = {
#     "watchlist": [
#         {"title": "Land Before Time"},
#         {"title": "Spirited Away"}
#     ],
#     "watched": [
#             {"title": "Lord of the Rings"},
#             {"title": "Parasyte"},
#             {"title": "Harry Potter"},
#             {"title": "Ready Player One"}
#     ]
# }
# title = "Land Before Time"

# 4th function
def watch_movie(user_data, title):
    move_movie = False
    index = 0
    movie = None
    for index in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][index]["title"]:
            move_movie = True
            movie_index = index
            movie = user_data["watchlist"][index]
            print(user_data["watchlist"][index])
    if move_movie:
        (user_data["watched"]).append(movie)
        del user_data["watchlist"][movie_index]
    return user_data
# watch_movie testing info, please leave commented incase it breaks
# watch_movie(user_data, title)


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# get_watched_avg_rating testing info, please leave commented incase it breaks
# user_data = {
#     "watchlist": [
#         {"title": "Land Before Time", "rating": 2},
#         {"title": "Spirited Away", "rating": 3}
#     ],
#     "watched": [
#             {"title": "Lord of the Rings", "rating":4},
#             {"title": "Parasyte", "rating":3},
#             {"title": "Harry Potter", "rating":1},
#             {"title": "Ready Player One", "rating":5}
#     ]
# }

# 1st function in Wave 2
def get_watched_avg_rating(user_data):
# created a variable for the sum of all ratings, the # of movies and the average
    movie_count = 0
    ratings_sum = 0
    ratings_avg = 0
# check if there are movies in "watched"
    if user_data["watched"]:
# loop through movies in watched
        for index in range(len(user_data["watched"])):
# update variables
            movie_count += 1
            ratings_sum += user_data["watched"][index]["rating"]
        ratings_avg = ratings_sum/movie_count
    return ratings_avg

# get_watched_avg_rating testing info, please leave commented incase it breaks
# get_watched_avg_rating(user_data)
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

