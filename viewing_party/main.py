from statistics import mode

# Wave 1

def create_movie(title, genre, rating):
    """
    Creates dictionary of movie title, genre, and rating
    """
    movie_dict = {}
    if title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    """
    Adds a movie to user's watched movies
    user_data is a dictionary with key "watched" and value []
    movie is dictionary from create_movie
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    Adds movie to user's list of movies to be watched
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    Moves movie from user's watchlist to watched movies list
    """
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == title:
            user_data["watchlist"].remove(movie_dict)
            user_data["watched"].append(movie_dict)
    return user_data

# Wave 2

def get_watched_avg_rating(user_data):
    """
    Calculates average rating from watched movies in user_data
    """
    total_rating = 0.0
    movie_count = 0
    average_rating = 0

    for movie_dict in user_data["watched"]:
        if user_data["watched"]:
            total_rating += movie_dict["rating"]
            movie_count += 1
            average_rating = total_rating / movie_count
    return average_rating

def get_most_watched_genre(user_data):
    """
    Returns the most frequent genre (mode) from watched movies
    in user_data
    """
    genres = []

    if user_data["watched"] == []:
        return None
    else:
        for movie_dict in user_data["watched"]:
            genres.append(movie_dict["genre"])
    # calculates most frequent element via mode method in statistics module
    most_watched_genre = mode(genres)
    return most_watched_genre

# Wave 3

def get_friends_watched_list(user_data):
    """
    Helper function to pull out list of friends watched movies from
    friends list in user data
    """
    friends_movie_list = user_data["friends"]
    friends_watched_list = []

    for friends_dict in friends_movie_list:
        for watched_dict in friends_dict["watched"]:
            friends_watched_list.append(watched_dict)
    return friends_watched_list

def get_unique_watched(user_data):
    """
    Gets movies unique to user's watched list
    (movies the user has watched but friends have not)
    """
    unique_user_movies = []
    # list of dictionaries of movies that friends have watched
    friends_watched_list = get_friends_watched_list(user_data)
    # list of dictionaries of movies that user has watched
    user_watched_list = []

    for movie_dict in user_data["watched"]:
        user_watched_list.append(movie_dict)

    for movie_dict in user_watched_list:
        if movie_dict not in friends_watched_list:
            unique_user_movies.append(movie_dict)

    return unique_user_movies

def get_friends_unique_watched(user_data):
    """
    Gets list of movies unique to friends' watched lists
    (movies friends have watched but user has not)
    """
    unique_friend_movies = []
    friends_watched_list = get_friends_watched_list(user_data)
    user_watched_list = user_data["watched"]

    for friend_dict in friends_watched_list:
        if friend_dict not in user_watched_list and\
            friend_dict not in unique_friend_movies:
            unique_friend_movies.append(friend_dict)
    return unique_friend_movies

# Wave 4

def get_available_recs(user_data):
    """
    Creates list of recommended movies if user has not watched,
    at least one of user's friends has watched, and user is subscribed to
    streaming service (host)
    """
    recommended_movies = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_watched_list(user_data)

    for watched_dict in friends_watched_list:
        if (watched_dict["title"] not in user_watched_list) and\
        watched_dict["host"] in user_data["subscriptions"] and\
        watched_dict not in recommended_movies:
            recommended_movies.append(watched_dict)
    return recommended_movies

# Wave 5

def get_new_rec_by_genre(user_data):
    """
    Creates list of recommended movies by genre if user has not watched it, one
    of user's friends has wathced it, and genre is the same as user's most
    frequently watched genre
    """
    recs_by_genre = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_watched_list(user_data)
    user_favorite_genre = get_most_watched_genre(user_data)

    for watched_dict in friends_watched_list:
        if (watched_dict["title"] not in user_watched_list) and\
        watched_dict["genre"] == user_favorite_genre and\
        watched_dict not in recs_by_genre:
            recs_by_genre.append(watched_dict)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    """
    Creates list of recommended movies if the movie is in user's
    favorites list and none of user's friends have watched it
    """
    recs_from_favorites = []
    user_favorite_list = user_data["favorites"]
    friends_watched_list = get_friends_watched_list(user_data)

    for favorite in user_favorite_list:
        if favorite not in friends_watched_list:
            recs_from_favorites.append(favorite)
    return recs_from_favorites
