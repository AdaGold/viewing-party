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

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# get_unique_watched testing info, please leave commented incase it breaks
user_data = {   'friends': [   {   'watched': [   {   'genre': 'Fantasy',
                                        'rating': 4.8,
                                        'title': 'The Lord of the Functions: '
                                                'The Fellowship of the '
                                                'Function'},
                                    {   'genre': 'Fantasy',
                                        'rating': 4.0,
                                        'title': 'The Lord of the Functions: '
                                                'The Return of the Value'},
                                    {   'genre': 'Fantasy',
                                        'rating': 4.0,
                                        'title': 'The Programmer: An '
                                                'Unexpected Stack Trace'},
                                    {   'genre': 'Horror',
                                        'rating': 3.5,
                                        'title': 'It Came from the Stack '
                                                'Trace'}]},
                {   'watched': [   {   'genre': 'Fantasy',
                                        'rating': 4.8,
                                        'title': 'The Lord of the Functions: '
                                                'The Fellowship of the '
                                                'Function'},
                                    {   'genre': 'Action',
                                        'rating': 2.2,
                                        'title': 'The JavaScript and the '
                                                'React'},
                                    {   'genre': 'Intrigue',
                                        'rating': 2.0,
                                        'title': 'Recursion'},
                                    {   'genre': 'Intrigue',
                                        'rating': 3.0,
                                        'title': 'Zero Dark Python'}]}],
'watched': [   {   'genre': 'Fantasy',
                    'rating': 4.8,
                    'title': 'The Lord of the Functions: The Fellowship of '
                            'the Function'},
                {   'genre': 'Fantasy',
                    'rating': 4.0,
                    'title': 'The Lord of the Functions: The Two '
                            'Parameters'},
                {   'genre': 'Fantasy',
                    'rating': 4.0,
                    'title': 'The Lord of the Functions: The Return of the '
                            'Value'},
                {   'genre': 'Action',
                    'rating': 2.2,
                    'title': 'The JavaScript and the React'},
                {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
                {   'genre': 'Intrigue',
                    'rating': 4.5,
                    'title': 'Instructor Student TA Manager'}]}


# 1st function in Wave 3

def get_unique_watched(user_data):
# code below does not work because of first if statement aint workin, try using sets
    user_only_movies = []

    for friend in user_data["friends"]:
        for movie in user_data["watched"]:
            if movie not in friend["watched"]:
                if movie in user_only_movies:
                    continue
                else:
                    user_only_movies.append(movie)

    return print(user_only_movies)

get_unique_watched(user_data)        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

