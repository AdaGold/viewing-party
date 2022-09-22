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

    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            avg_rating += movie["rating"]
        return avg_rating / len(user_data["watched"])
    return avg_rating


def get_most_watched_genre(user_data):
    most_watched_genre = None
    watched_genres = {}
    
    if len(user_data) > 0:
        for movie in user_data["watched"]:
            if movie["genre"] not in watched_genres:
                watched_genres[movie["genre"]] = 0
            else:
                watched_genres[movie["genre"]] += 1

        most_watched_frequency = 0
        for genre, frequency in watched_genres.items():
            if frequency > most_watched_frequency:
                most_watched_frequency = frequency
                most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_user_set(user_data):
    user_set = set()
    for movie in user_data["watched"]:
        user_set.add(movie["title"])
    return user_set


def get_friend_set(user_data):
    friend_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_set.add(movie["title"])
    return friend_set


def get_unique_watched(user_data):
    user_set = get_user_set(user_data)
    friend_set = get_friend_set(user_data)
    unique_set = user_set - friend_set

    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_set and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies


def get_friends_unique_watched(user_data):
    user_set = get_user_set(user_data)
    friend_set = get_friend_set(user_data)
    friends_unique_set = friend_set - user_set

    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friends_unique_set and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_recs = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    if len(user_data["watched"]) > 0:
        for movie in friends_unique_movies:
            if movie["rating"] >= 3.5:
                friends_recs.append(movie)

    return friends_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommendations = []
    friends_recs = get_available_recs(user_data)
    if len(user_data["watched"]) > 0 and len(friends_recs) > 0:
        most_watched_genre = get_most_watched_genre(user_data)
        for movie in friends_recs:
            if movie["genre"] == most_watched_genre:
                recommendations.append(movie)

    return recommendations


def get_rec_from_favorites(user_data):
    recommendations = []
    favorites_genres = {}

    if len(user_data["watched"]) > 0:
        for movie in user_data["favorites"]:
            if movie["genre"] not in favorites_genres:
                favorites_genres[movie["genre"]] = [movie]
            else:
                favorites_genres[movie["genre"]].append(movie)
        
        for genre in favorites_genres:
            recommendations.append(favorites_genres[genre][-1])

    return recommendations