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

def get_unique_watched(user_data):
    user_set = set()
    for movie in user_data["watched"]:
        user_set.add(movie["title"])

    friend_set = set()
    for friend_data in user_data["friends"]:
        for movie in friend_data["watched"]:
            friend_set.add(movie["title"])
    
    unique_set = user_set - friend_set

    unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_set and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies


def get_friends_unique_watched(user_data):
    user_set = set()
    for movie in user_data["watched"]:
        user_set.add(movie["title"])
    
    friend_set = set()
    for friend_data in user_data["friends"]:
        for movie in friend_data["watched"]:
            friend_set.add(movie["title"])
    
    friends_unique_set = friend_set - user_set

    friends_unique_movies = []
    for friend_data in user_data["friends"]:
        for movie in friend_data["watched"]:
            if movie["title"] in friends_unique_set and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_recs = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    if len(user_data["watched"]) == 0:
        return friends_recs

    for movie in friends_unique_movies:
        if movie["rating"] >= 3.5:
            friends_recs.append(movie)

    return friends_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommendations = []
    if len(user_data["watched"]) == 0:
        return recommendations
    
    friends_recs = get_available_recs(user_data)
    if len(friends_recs) == 0:
        return recommendations

    most_watched_genre = get_most_watched_genre(user_data)

    for movie in friends_recs:
        if movie["genre"] == most_watched_genre:
            recommendations.append(movie)
    
    return recommendations


def get_rec_from_favorites(user_data):
    # should return FANTASY_2b, INTRIGUE_2b
    # loop through all the movies, organize by genre
    # return genre_list[-1] and append to recommendations

    recommendations = []
    genres = {}

    if len(user_data["watched"]) == 0:
        return recommendations

    for movie in user_data["favorites"]:
        if movie["genre"] not in genres:
            genres[movie["genre"]] = [movie]
        else:
            genres[movie["genre"]].append(movie)
    
    for genre in genres:
        recommendations.append(genres[genre][-1])
    
    return recommendations