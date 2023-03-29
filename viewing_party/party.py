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
#         {"title": "Spirited Away"}git
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

#wave 2 
#function 2
def get_most_watched_genre(user_data):

    most_watched_genre = user_data.get("watched",[])
    
    if not most_watched_genre: 
        return None


    genres = {}
    for movie in most_watched_genre:
        genre = movie.get("genre")
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1

    most_watched_genre = max(genres, key=genres.get)

    return most_watched_genre #most viewed genre

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


#wave 3
#function 2


def get_friends_unique_watched(user_data):

    user_watched = set([movie["title"] for movie in user_data["watched"]])
    friends_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie not in friends_list:
                friends_list.append(movie)

    return friends_list

"""
does not remove duplicates
    user = user_data["watched"]
    friends = user_data["friends"] 

    friends_list = []

    #i = watched
    for i_dict in friends:
        movies_list = i_dict["watched"] 
        for movies_dict in movies_list:
            if movies_dict not in user:
                friends_list.append(movies_dict)
                if key,value in friends_list["title"]
    return friends_list
"""


#wave 4
#function 1

# def get_available_recs(user_data):
#     """
#     takes 1 parameter user_data
#     user_data field subcscriptions
#     value of subscriptions is list of string
#     represents the names of ea streaming service user has access
#     ea friend in friends has watched list
#     ea movie in watched list has host
#     host is string that says what streaming service is hosted on
#     determine list of recs nmovies
#     movie should be added to list only if 
#     user has not watched
#     atleast one user friend has watched
#     host of movie is service thats in users subscription 
#     return list of rec movies
#     """
#      amandas_data = {
#         "subscriptions": ["hulu", "disney+"],
#         "watched": [],
#         "friends": [
#             {
#                 "watched": [HORROR_1b]
#             },
#             {
#                 "watched": [FANTASY_3b]
#             }
#         ]
#     }
#     #subscription ['netflix','hulu','crunchyroll']
#     friends = [friend:[movie : "host"(watched list)]]
#     list_of_rec_movies = []

#     users_subscriptions = user_data[0]
#     #[friends][0][watched]
#     movies add to list if 
#     user has not watched
#     one friend has watched
#     host is a service users owns
#     return list_of_rec_movies
    


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

