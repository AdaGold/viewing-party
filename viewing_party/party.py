# ------------- WAVE 1 --------------------

from ast import If
from types import NoneType
from tests.test_constants import MOVIE_TITLE_1, USER_DATA_2


def create_movie(movie_title, genre, rating):


    movie = {}

    movie["title"] = movie_title
    movie["genre"] = genre
    movie["rating"] = rating
    
    for item in movie.values():
        if item == None:
            return None
    else:
        return movie

def add_to_watched(user_data, movie):

    user_data = {
    "watched": []
    }   
    copy = movie.copy()

    user_data["watched"].append(copy)
    
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": []
    }
    copy1 = movie.copy()
    
    user_data["watchlist"].append(copy1)

    return user_data

def watch_movie(user_data, title):



    for movie in user_data["watchlist"]:
        if title == movie['title']:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data
            

        
        





# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    
    sum = 0
    count = 0
    for movie in user_data["watched"]:
        sum += movie["rating"]
        count +=1
    if sum != 0:
        avg = sum / count
    else:
        avg = 0.0

    return avg

def get_most_watched_genre(user_data):
# will come back to this one to handle all test cases
    for movie in user_data["watched"]:
        if movie["genre"] == movie["genre"]:
            return movie["genre"]
        elif len(user_data["watched"]) == 0:
            return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    my_movie_list = []
    friends_movie_list = []
    unique_movie_list = []
    for movie_entry in user_data["watched"]:

        my_movie_list.append(movie_entry)
    
    for friend_watched_dict in user_data["friends"]:
        friend_watched_dict_list = friend_watched_dict["watched"]

        for movie_entry in friend_watched_dict_list:
            if movie_entry not in friends_movie_list:
                friends_movie_list.append(movie_entry)
            


    for my_movie in my_movie_list: 
        if my_movie not in friends_movie_list:
                unique_movie_list.append(my_movie)
        
            
    return unique_movie_list

    

def get_friends_unique_watched(user_data):

    friends_list = []
    user_list = []
    friends_unique_movies = []

    for movies in user_data["friends"][0]["watched"]:
        friends_list.append(movies)
    for movies in user_data["friends"][1]["watched"]:
        friends_list.append(movies)
    for movies in user_data["watched"]:
        user_list.append(movies)
    for movie in friends_list:
        if movie not in user_list and movie not in friends_unique_movies:
            friends_unique_movies.append(movie)
    
    return friends_unique_movies
    

    

# ------------- WAVE 4 --------------------
# ----------------------------------------- 

def get_available_recs(user_data):

    movie_recs = []
    friend_list = []
    user_subscriptions = user_data["subscriptions"]
    # Loop through friends watched movies to get all movies that friends watched in one liist
    for movies1 in user_data["friends"][0]["watched"]:
        friend_list.append(movies1)
    for movies in user_data["friends"][1]["watched"]:
        friend_list.append(movies)
# Check to make sure friends movie is not in user movies, and check to make sure "host" is in user subscriptions
    for friend in friend_list:
        if friend not in user_data["watched"] and friend["host"] in user_subscriptions:
            movie_recs.append(friend)
    return movie_recs








# -----------------------------------------
# ------------- WAVE 5 -------------------
def get_new_rec_by_genre(user_data):

    list_of_genres = []
    genres = {}
    most_watched_genre = ""
    new_val = []
    friends_list = []
    new_recs = []

  


# Move user genres to a list to get most watched genre
    for movie in user_data["watched"]:
        list_of_genres.append(movie["genre"])

# Add genre counts to a dictionary with value being how many times the genre appears in a list.
    for genre in list_of_genres:
        genres[genre] = genres.get(genre,0) + 1

# getting highest value from dict
    new_val = genres.values()
    if len(new_val) > 0:
        max_val = max(new_val)
    for genre in genres:
        if genres[genre] == max_val:
            most_watched_genre = genre

    for movie in user_data["friends"][0]["watched"]:
        friends_list.append(movie)
    for movie in user_data["friends"][1]["watched"]:
        friends_list.append(movie)

    for movies in friends_list:
        if movies not in user_data["watched"] and movies["genre"] == most_watched_genre:
            new_recs.append(movies)
    return new_recs

def get_rec_from_favorites(user_data):
    user_favorites = []
    friend_list = []
    movie_recs = []
    

    for movies in user_data["favorites"]:
        user_favorites.append(movies)
    if len(user_data["friends"]) > 0:
        for friends in user_data["friends"][0]["watched"]:
            friend_list.append(friends)
        for friends in user_data["friends"][1]["watched"]:
            friend_list.append(friends)

    for movies in user_favorites:
        if movies not in friend_list:
            movie_recs.append(movies)
    return movie_recs



