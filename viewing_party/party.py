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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

