# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):

    new_movie = {}

    if movie_title and genre and rating:
        new_movie["title"] =  movie_title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
    return None

def add_to_watched(user_data, movie):
    if user_data["watched"]:
        user_data["watched"].append(movie)
    else:
        user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    if user_data["watchlist"]:
        user_data["watchlist"].append(movie)
    else:
        user_data["watchlist"] = [movie]
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
    if user_data["watched"]:
        for movie in user_data["watched"]:
            if movie["genre"] in genre_count:
                genre_count[movie["genre"]] += 1
            else:
                genre_count[movie["genre"]] = 1
    
        highest_rated_count = max(genre_count.values())
        for genre, count in genre_count.items():
            if count == highest_rated_count:
                return genre

    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

