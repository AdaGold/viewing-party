# ------------- WAVE 1 --------------------

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
    #user_data = {
    #    "watchlist": [],
    #    "watched": []
    #}
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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

