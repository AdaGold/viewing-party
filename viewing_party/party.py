from statistics import mean

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): 
    # if any of the vars are None, return None
    if not title or not genre or not rating:
        return None
    
    # create new dict
    new_movie = {
        "title": title,
        "genre": genre,
        "rating":rating,
    }

    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    # Parse through the movies in watchlist
    for movie in user_data["watchlist"]:

        # if title == the movie title then operate on it
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    # return modified user_data
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
#create function get_watched_avg_rating(user_data)
        # user data is dict with 'watched' [{}]
    if user_data["watched"] == []:
        average_rating = 0.0
        return average_rating

    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie['rating'])
    average_rating = mean(ratings)
    return average_rating

def get_most_watched_genre(user_data):
    # handles empty watchlist
    if user_data["watched"] == []:
        return None
    
    genres = []
    # iterate through user-data to fine movie value for watched
    for movie in user_data["watched"]:
        # add value of genre to variable genres
        genres.append(movie["genre"])
        
    # use count to find which genres repeat most and delete others
    popular_genre = max(set(genres), key = genres.count)
    
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # get all the titels for users_watched
    user_watched_titles = set([movie["title"] for movie in user_data['watched']])

    # build set of all friends watched
    friends_watched_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_titles.append(movie["title"])
    friends_watched_titles = set(friends_watched_titles)

    # find unique friends watched
    unique_watched_titles = user_watched_titles.difference(friends_watched_titles)
    unique_watched_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_watched_titles:
            unique_watched_movies.append(movie)

    return unique_watched_movies    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

