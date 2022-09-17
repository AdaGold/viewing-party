# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]
    return avg_rating / len(user_data["watched"])


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

