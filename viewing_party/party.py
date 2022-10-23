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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

