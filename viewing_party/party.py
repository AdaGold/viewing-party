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
    if len(user_data["watched"]) == 0:
        return avg_rating

    for movie in user_data["watched"]:
        avg_rating += movie["rating"]
    return avg_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):
    watched_genres = {}
    
    if len(user_data) == 0:
        return None
    
    for movie in user_data["watched"]:
        if movie["genre"] not in watched_genres:
            watched_genres[movie["genre"]] = 0
        else:
            watched_genres[movie["genre"]] += 1
    
    most_watched = 0
    most_watched_genre = None
    
    for genre, frequency in watched_genres.items():
        if frequency > most_watched:
            most_watched = frequency
            most_watched_genre = genre
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

