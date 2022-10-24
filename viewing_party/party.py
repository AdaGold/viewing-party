# ------------- WAVE 1 --------------------
import statistics

def create_movie(title, genre, rating):
    new_movie = dict()
    if title == None or genre == None or rating == None:
        return None
    else:
     new_movie["title"] = title
     new_movie["genre"] = genre
     new_movie["rating"] = rating
     return new_movie

def add_to_watched(user_data, movie):
    updated_user_data = {
        "watched": []
    }
    updated_user_data["watched"].insert(0,movie)
    return updated_user_data

def add_to_watchlist(user_data, movie):
    updated_user_data = {
        "watchlist": []
    }
    updated_user_data["watchlist"].insert(0,movie)
    return updated_user_data

def watch_movie(user_data, movie_title):
    if movie_title == None or user_data["watchlist"] == None:
        return user_data
    else: 
        for movie in user_data["watchlist"]:
            if movie["title"] == movie_title:
                user_data["watched"].insert(0,movie)
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
    else:
        for element in user_data["watched"]:
            sum_ratings += element["rating"]
        avg_rating = sum_ratings/len(user_data["watched"])
        return avg_rating

def get_most_watched_genre(user_data):
    most_watched_genre = ""
    list_of_genre = list()
    if len(user_data["watched"]) == 0:
        return None
    else:
        for i in range(len(user_data["watched"])):
            list_of_genre.append(user_data["watched"][i]["genre"])
        most_watched_genre = statistics.mode(list_of_genre)
        return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_movie_list = list()
    unique_movies = list()
    if len(user_data["watched"]) == 0:
        unique_movies = []
        return unique_movies
    else:
        for i in range(len(user_data["friends"])):
            for j in range(len(user_data["friends"][i]["watched"])):
                friends_movie_list.append(user_data["friends"][i]["watched"][j]["title"])
        friends_movie_set = set(friends_movie_list)
        for k in range(len(user_data["watched"])):
            if user_data["watched"][k]["title"] not in friends_movie_set:
                unique_movies.append(user_data["watched"][k])
        return unique_movies
    
def get_friends_unique_watched(user_data):
    friends_movie_list = list()
    friends_unique_movies = list()
    if len(user_data["watched"]) == 0:
        for i in range(len(user_data["friends"])):
            for j in range(len(user_data["friends"][i]["watched"])):
                if (friends_movie_list[i] not in friends_unique_movies):
                    friends_movie_list.append(user_data["friends"][i]["watched"][j])
        #friends_unique_movies = set(friends_movie_list)
        return friends_unique_movies
    else:
        for i in range(len(user_data["friends"])):
            for j in range(len(user_data["friends"][i]["watched"])):
                friends_movie_list.append(user_data["friends"][i]["watched"][j])
        for k in range(len(friends_movie_list)):
            if (friends_movie_list[k] not in user_data["watched"]) and ((friends_movie_list[k] not in friends_unique_movies)):
                friends_unique_movies.append(friends_movie_list[k])
        #friends_unique_movies_set = set(friends_unique_movies)
        return friends_unique_movies#_set
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

