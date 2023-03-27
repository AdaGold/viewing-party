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


# create fun named add_to_watchlist
# 2 param, user_data & movie
# add movie to user_data of watch_list
# return user_data
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

