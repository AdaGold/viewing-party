# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    else:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating

    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    new_watchlist = []
    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]:
            add_to_watched(user_data, user_data["watchlist"][i])
        else:
            new_watchlist.append(user_data["watchlist"][i])
    user_data["watchlist"] = new_watchlist

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings_sum = 0
    movie_count = 0

    if not user_data["watched"]:
        return 0

    for movie in user_data["watched"]:
        ratings_sum += movie["rating"]
        movie_count += 1

    return ratings_sum/movie_count


def get_most_watched_genre(user_data):
    genre_count = {}

    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1

    highest_rated_count = max(genre_count.values())
    for genre, count in genre_count.items():
        if count == highest_rated_count:
    
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
