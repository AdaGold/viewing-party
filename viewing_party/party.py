# ------------- WAVE 1 --------------------

"""
    first function create movie
    function takes 3 paramaters/attributes, titles, genre, rating
    if three attributers are truthy, return dictionary
    if title falsy, genre is falsy or rating is falsy, these should return none
    
"""

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

    
    
def add_to_watched(user_data, movie):
    
    if not movie:
        user_data["watched"].append(movie)

def add_to_watchlist(user_data, movie):

    watchlist = user_data.get("watchlist", [])

    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    
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

