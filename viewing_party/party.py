# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {"title": title, "genre": genre, "rating": rating}


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    new_watchlist = []

    for i in range(len(watchlist)):
        if title == watchlist[i]["title"]:
            add_to_watched(user_data, watchlist[i])
        else:
            new_watchlist.append(watchlist[i])
    user_data["watchlist"] = new_watchlist

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0

    ratings_sum = sum([movie["rating"] for movie in user_data["watched"]])
    movie_count = len(user_data["watched"])

    return ratings_sum/movie_count


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genre_count = {}

    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1

    return max(genre_count, key=genre_count.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    
    friends_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles.append(movie["title"])

    user_unique_movies = []
    for movie in user_data["watched"]:
        if movie["title"] not in set(friends_titles):
            user_unique_movies.append(movie)

    return user_unique_movies


def get_friends_unique_watched(user_data):    

    user_titles = []
    for movie in user_data["watched"]:
        user_titles.append(movie["title"])

    friends_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles.append(movie["title"])

    friends_unique_titles = []
    for item in set(friends_titles):
        if item not in set(user_titles):
            friends_unique_titles.append(item)

    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in set(friends_unique_titles):
                friends_unique_movies.append(movie)

    friends_unique_movies_no_duplicates = []
    for movie in friends_unique_movies:
        if movie not in friends_unique_movies_no_duplicates:
            friends_unique_movies_no_duplicates.append(movie)

    return friends_unique_movies_no_duplicates

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):

    movies_to_consider = get_friends_unique_watched(user_data)
    subscriptions_owned = user_data["subscriptions"]

    return [movie for movie in movies_to_consider
            if movie["host"] in subscriptions_owned]

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    movies_to_consider = get_friends_unique_watched(user_data)

    user_watched_genres = []
    for k in user_data["watched"]:
        user_watched_genres.append(k["genre"])

    if len(user_watched_genres) == 0:
        return []

    most_frequent_genre = max(set(user_watched_genres), key=user_watched_genres.count)

    list_of_recommended_movies = []
    for movie in movies_to_consider:
        if movie["genre"] == most_frequent_genre:
            list_of_recommended_movies.append(movie)

    return list_of_recommended_movies


def get_rec_from_favorites(user_data):

    user_unique_watched_movies = get_unique_watched(user_data)
    favorite_movies = user_data["favorites"]

    return [movie for movie in user_unique_watched_movies
            if movie in favorite_movies]
