from statistics import mean

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): 
    # if any of the vars are None, return None
    if not title or not genre or not rating:
        return None
    
    # create new dict
    new_movie = {
        "title": title,
        "genre": genre,
        "rating":rating,
    }

    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    # Parse through the movies in watchlist
    for movie in user_data["watchlist"]:

        # if title == the movie title then operate on it
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    # return modified user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    # deal w/ empty list of watched data
    if user_data["watched"] == []:
        average_rating = 0.0
        return average_rating

    # creats list of all ratings
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie['rating'])
        
    # calculates average
    average_rating = mean(ratings)
    return average_rating


def get_most_watched_genre(user_data):
    # handles empty watchlist
    if user_data["watched"] == []:
        return None
    
    genres = []
    # iterate through user-data to fine movie value for watched
    for movie in user_data["watched"]:
        # add value of genre to variable genres
        genres.append(movie["genre"])
        
    # use count to find which genres repeat most and delete others
    popular_genre = max(set(genres), key=genres.count)
    
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_friends_watched_titles(user_data):
    return set(movie["title"] for friend in user_data["friends"] for movie in friend["watched"])

def get_user_watched_titles(user_data):
    return set([movie["title"] for movie in user_data['watched']])

def get_unique_watched(user_data):
    # get all the titles for users_watched
    user_watched_titles = get_user_watched_titles(user_data)

    # build set of all friends watched
    friends_watched_titles = get_friends_watched_titles(user_data)

    # find unique user watched
    unique_user_watched_titles = user_watched_titles - friends_watched_titles
    unique_user_watched_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_user_watched_titles:
            unique_user_watched_movies.append(movie)

    return unique_user_watched_movies    


def get_friends_unique_watched(user_data):
    # get all the titles for users_watched
    user_watched_titles = get_user_watched_titles(user_data)
    
    # build set of all friends watched
    friends_watched_titles = get_friends_watched_titles(user_data)
    
    # find unique friends watched
    friends_unique_watched_titles = friends_watched_titles - user_watched_titles
    
    # create non duplicated list of all the movies friends have watched and user
    # has not.  Use a seperate list added_titles to be sure of no dups.
    friends_unique_watched_movies = []
    added_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friends_unique_watched_titles:
                if movie["title"] not in added_titles:
                    friends_unique_watched_movies.append(movie)
                    added_titles.append(movie["title"])

    return friends_unique_watched_movies    


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    # create subscriotions, user_watched, and friends_watched lists
    subscriptions = set(user_data["subscriptions"])
    user_watched_titles = get_user_watched_titles(user_data)
    friends_watched = get_friends_unique_watched(user_data)

    # find the movies that are not in user watched and that are available with subscriptions
    recommended = []
    for movie in friends_watched:
        if movie['title'] not in user_watched_titles and movie['host'] in subscriptions:
            recommended.append(movie)
    return recommended



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    # get most freq genere and friends watched.  
    most_frequent_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)

    # find recommendations if user hasnt watched and genre is most freq
    recommendations = []
    for movie in friends_watched:
        if movie not in user_data['watched'] and movie['genre'] == most_frequent_genre:
            recommendations.append(movie)
    return recommendations


def get_rec_from_favorites(user_data):
    # create favorites and user_watched_titles
    favorites = user_data["favorites"]
    user_watched_titles = [movie['title'] for movie in get_unique_watched(user_data)]

    # get recommendations if the movie is in faves and unique user movies
    recommendations = []
    for movie in favorites:
        if movie['title'] in user_watched_titles:
            recommendations.append(movie)

    return recommendations