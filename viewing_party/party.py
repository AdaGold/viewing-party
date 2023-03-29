# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
        "title": title,
        "genre": genre,
        "rating": rating
        }
        return movie
    return None


def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = 0
    movie_count = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            ratings += (movie["rating"])
            movie_count += 1
        avg_rating = ratings/movie_count
        return avg_rating
    return ratings

def get_most_watched_genre(user_data):
    if user_data["watched"]:
        genre_frequencies = {}
        for movie in user_data["watched"]:
            genre_frequencies[movie["genre"]] = 0
        for movie in user_data["watched"]:
            genre_frequencies[movie["genre"]] += 1

        highest_count = max(genre_frequencies.values())
        for genre, count in genre_frequencies.items():
            if count == highest_count:
                return genre

    return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    friends_movies = []
    for friend in user_data["friends"]:
        friends_movies+=(friend["watched"])
    
    for movie in user_data["watched"]:
        if not movie in friends_movies:
            unique_movies.append(movie)
        
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friends_movies = []
    for friend in user_data["friends"]:
        friends_movies +=friend["watched"]
    for movie in friends_movies:
        if not movie in user_data["watched"]:
            if not movie in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"] and movie not in movie_recommendations:
                movie_recommendations.append(movie)
    return movie_recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
"""A movie should be added to this list if and only if:
  - The user has not watched it
  - At least one of the user's friends has watched
  - The `"genre"` of the movie is the same as the user's most frequent genre
- Return the list of recommended movies"""
def get_new_rec_by_genre(user_data):
    top_genre = get_most_watched_genre(user_data)
    recommended_movies = []
    friends_movies = []
    for friend in user_data["friends"]:
        friends_movies +=friend["watched"]
    for movie in friends_movies:
        if movie not in user_data["watched"] and movie["genre"] == top_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    pass