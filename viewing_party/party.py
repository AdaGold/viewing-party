# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if not (title and genre and rating):
        return None
    else:
        movie = { "title" : title,
                    "genre" : genre,
                    "rating" : rating}
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

# Wave 2
# Create a function named get_watched_avg_rating. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries
# This represents that the user has a list of watched movies
# Calculate the average rating of all movies in the watched list
# The average rating of an empty watched list is 0.0
# return the average rating
# Create a function named get_most_watched_genre. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries. Each movie dictionary has a key "genre".
# This represents that the user has a list of watched movies. Each watched movie has a genre.
# The values of "genre" is a string.
# Determine which genre is most frequently occurring in the watched list
# return the genre that is the most frequently watched
# If the value of "watched" is an empty list, get_most_watched_genre should return None.


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Create a function named get_unique_watched. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# This represents that the user has a list of watched movies and a list of friends
# The value of "friends" is a list
# Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
# Each movie dictionary has a "title".
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies
# Create a function named get_friends_unique_watched. This function should...
# take one parameter: user_data
# the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
# This represents that the user has a list of watched movies and a list of friends
# The value of "friends" is a list
# Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
# Each movie dictionary has a "title".
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# Return a list of dictionaries, that represents a list of movies

        
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









