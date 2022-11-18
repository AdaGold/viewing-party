# ------------- WAVE 1 --------------------
import statistics

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 
    new_movie = dict()
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    if not title or not user_data["watchlist"]:
        return user_data
    for i in range(len(user_data["watchlist"])):
        movie = user_data["watchlist"][i]
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    sum_ratings = 0
    if len(user_data["watched"]) == 0:
        return 0.0
    for element in user_data["watched"]:
        sum_ratings += element["rating"]
    avg_rating = sum_ratings/len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    most_watched_genre = ""
    list_of_genre = list()
    for movie in user_data["watched"]:
        list_of_genre.append(movie["genre"])
    most_watched_genre = statistics.mode(list_of_genre)
    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    if not user_data["watched"]:
        return []
    friends_movie_set = set()
    unique_movies = list()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_set.add(movie["title"])
    for user_movie in user_data["watched"]:
        if user_movie["title"] not in friends_movie_set:
            unique_movies.append(user_movie)     
    return unique_movies
    
def get_friends_unique_watched(user_data):
    if not user_data["watched"]:
        return []
    friends_unique_movies = list()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if ( movie not in user_data["watched"] and 
                movie not in friends_unique_movies):
                    friends_unique_movies.append(movie)
    return friends_unique_movies     
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_friends_movie = get_friends_unique_watched(user_data)
    if ( not user_data["watched"] or 
        not unique_friends_movie or 
        not user_data["subscriptions"]):
            return []
    list_of_recommended_movies = list()
    for movie in unique_friends_movie:
        if movie["host"] in user_data["subscriptions"]:
            list_of_recommended_movies.append(movie)
    return list_of_recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    if not user_data["watched"]:
        return []
    list_of_genre = get_most_watched_genre(user_data)
    list_of_movies = get_friends_unique_watched(user_data)
    if not list_of_movies or not list_of_genre:
        return []
    recommended_movies = list()
    for movie in list_of_movies:
        if movie["genre"] == list_of_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    if not user_data["watched"]:
        return []
    recommended_movies = list()
    unique_movies = get_unique_watched(user_data)
    for movie in unique_movies:
        if movie in user_data["favorites"]:
            recommended_movies.append(movie)  
    return recommended_movies