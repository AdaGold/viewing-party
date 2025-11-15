# 1st function in Wave 1
def create_movie(title, genre, rating):

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


# 2nd function in Wave 1
def add_to_watched(user_data, movie):

    (user_data["watched"]).append(movie)
    return user_data


# 3rd function in Wave 1
def add_to_watchlist(user_data, movie):

    watchlist = user_data.get("watchlist", [])

    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    
    return user_data


# 4th function in Wave 1
def watch_movie(user_data, title):

    move_movie = False
    index = 0
    movie = None

    for index in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][index]["title"]:
            move_movie = True
            movie_index = index
            movie = user_data["watchlist"][index]
            print(user_data["watchlist"][index])
    if move_movie:
        (user_data["watched"]).append(movie)
        del user_data["watchlist"][movie_index]
    return user_data


# 1st function in Wave 2
def get_watched_avg_rating(user_data):

    movie_count = 0
    ratings_sum = 0
    ratings_avg = 0

    if user_data["watched"]:

        for index in range(len(user_data["watched"])):

            movie_count += 1
            ratings_sum += user_data["watched"][index]["rating"]
        ratings_avg = ratings_sum/movie_count
    return ratings_avg


# 2nd function in Wave 2
def get_most_watched_genre(user_data):

    most_watched_genre = user_data.get("watched",[])
    
    if not most_watched_genre: 
        return None

    genres = {}
    for movie in most_watched_genre:
        genre = movie.get("genre")
        if genre in genres:
            genres[genre] += 1
        else:
            genres[genre] = 1

    most_watched_genre = max(genres, key=genres.get)

    return most_watched_genre 


# 1st function in Wave 3
def get_unique_watched(user_data):

    friends_watched_list = []
    friends_watched_set = None
    friends_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
            friends_watched_set = set(friends_watched_list)

    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_set and movie not in friends_list:
            friends_list.append(movie)

    return friends_list


# 2nd function in Wave 3
def get_friends_unique_watched(user_data):

    user_watched = set([movie["title"] for movie in user_data["watched"]])
    friends_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in user_watched and movie not in friends_list:
                friends_list.append(movie)

    return friends_list


# 1st function in Wave 4
def get_available_recs(user_data):

    unseen_by_user = get_friends_unique_watched(user_data)
    user_subscriptions = user_data["subscriptions"]
    available_recs = []

    for movie in unseen_by_user:
        if movie["host"] in user_subscriptions:
            available_recs.append(movie)
    return available_recs


#1st function Wave 5
def get_new_rec_by_genre(user_data):

    user_watched = set([movie["title"] for movie in user_data["watched"]])
    friends_unique_watched = get_friends_unique_watched(user_data)

    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1
    best_genre = None
    best_genre_count = 0
    for genre, count in genre_count.items():
        if count > best_genre_count:
            best_genre = genre
            best_genre_count = count

    recommended_movies = []
    for movie in friends_unique_watched:
        if movie["title"] not in user_watched and movie["genre"] == best_genre:
            recommended_movies.append(movie)

    return recommended_movies


# 2ND function in Wave 5
def get_rec_from_favorites(user_data):
    
    user_favorites = user_data["favorites"]
    recommended_movies = []

    if user_data["friends"] == []:
        return user_favorites
    else:
        unseen_by_friends = get_unique_watched(user_data)
        for movie in unseen_by_friends:
            if movie in user_favorites:
                recommended_movies.append(movie)
        return recommended_movies