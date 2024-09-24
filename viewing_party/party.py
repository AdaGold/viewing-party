# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    new_movie_info = {"title": title, "genre": genre, "rating": rating}
    return new_movie_info

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
    return user_data

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    
    total_movie_ratings = 0

    for movie_rating in user_data["watched"]:
        total_movie_ratings += movie_rating["rating"]

    average_movie_rating = total_movie_ratings / len(user_data["watched"])

    return average_movie_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    frequency_of_genre_index = {}
    max_frequency = 0
    most_watched_genre = None

    for single_movie in user_data["watched"]:
        genre_type = single_movie.get("genre")
        if genre_type:
            frequency_of_genre_index[genre_type] = frequency_of_genre_index.get(genre_type,0) + 1
            if frequency_of_genre_index[genre_type] > max_frequency:
              max_frequency = frequency_of_genre_index[genre_type]
              most_watched_genre = genre_type

    return most_watched_genre

def get_unique_watched (user_data):
    my_unique_movies = []
    my_friends_unique = set()
    
    if not user_data["watched"]:
        return []
  
    for my_friends in user_data["friends"]:
        my_friends_unique.update(movie["title"] for movie in my_friends["watched"] if "title" in movie)
    for movie in user_data["watched"]:
        if "title" in movie and movie["title"] not in my_friends_unique:
            my_unique_movies.append(movie)

    return my_unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []  
    my_friends_unique = set() 

    for my_friend in user_data["friends"]:
        for movie in my_friend["watched"]:
            if "title" in movie:
                my_friends_unique.add(movie["title"])

    watched_titles = {movie["title"] for movie in user_data["watched"] if "title" in movie}

    for my_friend in user_data["friends"]:
        for movie in my_friend["watched"]:
            if movie["title"] in my_friends_unique and movie["title"] not in watched_titles:
                friends_unique_movies.append(movie)
                my_friends_unique.remove(movie["title"])  

    return friends_unique_movies
'''

# Wave 3 READ_ME_INSTRUCTIONS

# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies


# ### Wave 4

# # def get_avaialable_recs(user_data):
# #     subscriptions = ""

# 1. Create a function named `get_available_recs`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies

# ### Wave 5

# 1. Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies
# '''
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# '''