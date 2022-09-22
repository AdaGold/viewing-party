# ------------- WAVE 1 --------------------

from tests.test_constants import clean_wave_2_data


def create_movie(title, genre, rating):
    movie_info = {}
    keys = ["title", "genre", "rating"]
    values = [title, genre, rating]
    for i in range(len(keys)):
        if values[i] == None:
            return None
        movie_info[keys[i]]=values[i]     
    return movie_info

def add_to_watched(user_data, movie):
    for key in user_data: 
        user_data[key]=[movie]
    return user_data

def add_to_watchlist(user_data, movie):
    for key in user_data: 
        user_data[key]=[movie]
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    ratings_sum = 0

    if watched_list == []:
            return 0.0

    for movie in watched_list:
        ratings_sum += movie["rating"]
        average = ratings_sum / len(watched_list)
    return average

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    genre_list = []

    if watched_list == []:
        return None
    
    for movie in watched_list:
        genre_list.append(movie["genre"])
    
    top_genre = max(set(genre_list), key=genre_list.count)
    return top_genre

        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched_list = user_data["watched"]
    friend_list = user_data["friends"]

    for value in friend_list:
        #print(value)
        for movie in value.values():
            print(movie)
    
        





    # for movie in watched_list:
    #     for friend in friend_watch_list:
    #         for movie2 in friend["watched"]:
    #             print(movie2["title"])
                
                

    #     if movie["title"] not in friend_watch_list:
    #         unique.append(movie)
    # return unique
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

