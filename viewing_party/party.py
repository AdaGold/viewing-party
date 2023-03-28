# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
        "title": title,
        "genre": genre,
        "rating": rating
        }
        return movie
    return None


def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = 0
    movie_count = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            ratings += (movie["rating"])
            movie_count += 1
        avg_rating = ratings/movie_count
        return avg_rating
    return ratings

def get_most_watched_genre(user_data):
    if user_data["watched"]:
        genre_frequencies = {}
        for movie in user_data["watched"]:
            genre_frequencies[movie["genre"]] = 0
        for movie in user_data["watched"]:
            genre_frequencies[movie["genre"]] += 1

        highest_count = max(genre_frequencies.values())
        for genre, count in genre_frequencies.items():
            if count == highest_count:
                return genre

    return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    pass

def get_friends_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass