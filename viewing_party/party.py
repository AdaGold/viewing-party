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


def get_unique_watched(user_data):
    friends_watched = []
    list_of_movies = []

    for i in user_data["friends"]:
        for j in i["watched"]:
            friends_watched.append(j["title"])

    for i in user_data["watched"]:
        if i["title"] not in set(friends_watched):
            list_of_movies.append(i)

    return list_of_movies


def get_friends_unique_watched(user_data):
    list_movies_titles = []
    friends_watched = []
    user_watched = []
    list_of_movies = []

    for k in user_data["watched"]:
        user_watched.append(k["title"])

    for i in user_data["friends"]:
        for j in i["watched"]:
            friends_watched.append(j["title"])

    for item in set(friends_watched):
        if item not in set(user_watched):
            list_movies_titles.append(item)

    for i in user_data["friends"]:
        for j in i["watched"]:
            if j["title"] in set(list_movies_titles):
                list_of_movies.append(j)

    final_list = []
    for movie in list_of_movies:
        if movie not in final_list:
            final_list.append(movie)

    return final_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    recommended_movies = []

    movies_to_consider = get_friends_unique_watched(user_data)
    subscriptions_owned = user_data["subscriptions"]

    for movie in movies_to_consider:
        if movie["host"] in subscriptions_owned:
            recommended_movies.append(movie)

    return recommended_movies

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