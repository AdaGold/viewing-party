# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not (title and genre and rating):
        return None
    else:
        movie = { "title" : title,
                "genre" : genre,
                "rating" : rating
                }
        return movie
    
def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break

    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_list = []
    if not user_data["watched"]:
        return 0.0
    for movie in user_data["watched"]:
        rating_list.append(movie["rating"])
    average_rating = sum(rating_list) / len(rating_list)
    return average_rating


def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    most_watched_genre_frequency = 0
    most_watched_genre = genre_list[0]
    for genre in genre_list:
        genre_frequency = genre_list.count(genre)
        if genre_frequency > most_watched_genre_frequency:
            most_watched_genre_frequency = genre_frequency
            most_watched_genre = genre

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_watched_titles =[]
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])
    
    friends_watched_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_watched_titles:
                friends_watched_titles.append(movie["title"])
    
    user_unique_titles = []
    for title in user_watched_titles:
        if title not in friends_watched_titles:
            user_unique_titles.append(title)
    
    user_unique_movies = []
    for title in user_unique_titles:
        for movie in user_data["watched"]:
            if movie["title"] == title:
                user_unique_movies.append(movie)

    return user_unique_movies


def get_friends_unique_watched(user_data):
    
    user_watched_titles =[]
    for movie in user_data["watched"]:
        user_watched_titles.append(movie["title"])
    
    friends_watched_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_watched_titles:
                friends_watched_titles.append(movie["title"])
    
    friends_unique_titles = []
    for title in friends_watched_titles:
        if title not in user_watched_titles:
            friends_unique_titles.append(title)
    
    friends_unique_movies = []
    for title in friends_unique_titles:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie["title"] == title and movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)

    return friends_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# Wave 4
# Create a function named get_available_recs. This function should...
# take one parameter: user_data
# user_data will have a field "subscriptions". The value of "subscriptions" is a list of strings
# This represents the names of streaming services that the user has access to
# Each friend in "friends" has a watched list. Each movie in the watched list has a "host", which is a string that says what streaming service it's hosted on
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"
# Return the list of recommended movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Wave 5
# Create a function named get_new_rec_by_genre. This function should...
# take one parameter: user_data
# Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies
# Create a function named get_rec_from_favorites. This function should...
# take one parameter: user_data
# user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
# This represents the user's favorite movies
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The movie is in the user's "favorites"
# None of the user's friends have watched it
# Return the list of recommended movies









