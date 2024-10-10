# ---------------------------------------------------- WAVE 1 ----------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------

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
    
    new_copy_watchlist = []

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            add_to_watched(user_data, movie)
        else:
            new_copy_watchlist.append(movie)
    
    user_data["watchlist"] = new_copy_watchlist
    return user_data

# ---------------------------------------------------- WAVE 2 ----------------------------------------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0
    
    total_movie_ratings = 0

    for movie_rating in user_data["watched"]:
        total_movie_ratings += movie_rating["rating"]

    average_movie_rating = total_movie_ratings / len(user_data["watched"])

    return average_movie_rating

def get_most_watched_genre(user_data):
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

# ---------------------------------------------------- WAVE 3 ----------------------------------------------------

def get_unique_watched(user_data):
    if not user_data["watched"]:
        return []
  
    my_friends_unique = {movie["title"] for my_friends in user_data["friends"] 
                         for movie in my_friends["watched"]}
    
    my_unique_movies = [movie for movie in user_data["watched"] 
                        if movie["title"] not in my_friends_unique]   

    return my_unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    my_movie_titles = [] 
    
    my_movie_titles = [movie["title"] for movie in user_data["watched"]]

    for my_friend in user_data["friends"]:           
        for movie in my_friend["watched"]:
            if movie["title"] not in my_movie_titles and movie not in friends_unique_movies:
                friends_unique_movies.append(movie) 

    return friends_unique_movies

# ---------------------------------------------------- WAVE 4 ----------------------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    user_watched_titles = set()
    
    for movie in user_data.get('watched', []):
        user_watched_titles.add(movie['title'])

    user_subscriptions = set(user_data.get('subscriptions', []))
    for movie in friends_unique_movies:
        if movie['host'] in user_subscriptions and movie['title'] not in user_watched_titles:
            if movie not in recommended_movies:
                recommended_movies.append(movie)
    
    return recommended_movies

# ---------------------------------------------------- WAVE 5 ----------------------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    recommended_movie = [movie for movie in friends_unique_watched
                         if movie["genre"] == most_watched_genre]

    return recommended_movie

def get_rec_from_favorites(user_data):
    my_friends_watched = set()

    my_friends_watched = [movie["title"] for my_friends in user_data["friends"] 
                          for movie in my_friends["watched"]]   

    recommended_movie = [movie for movie in user_data["favorites"] 
                         if movie["title"] not in my_friends_watched]

    return recommended_movie