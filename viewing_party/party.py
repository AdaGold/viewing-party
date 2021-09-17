#WAVE 1
def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    else:   
        new_movie = {"title": movie_title, "genre": genre, "rating": rating}
        return new_movie

def add_to_watched(user_data, movie):
    watched_list = user_data["watched"]
    watched_list.append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    add_watchlist = user_data["watchlist"]
    add_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    movies_watched = user_data["watched"]
    movie_to_watch = user_data["watchlist"]

    for movie in movie_to_watch: #should be singular "movie"
        if title == movie["title"]:
            movie_to_watch.remove(movie)
            movies_watched.append(movie)
    return user_data #no else statement needed

#WAVE 2
def get_watched_avg_rating(user_data):
    if user_data["watched"] == []:
        return 0.0
    else:
        ratings_total = 0
    for rating in user_data["watched"]:
        ratings_total += (rating["rating"])
    list_count = (len(user_data["watched"]))
    average = ratings_total/list_count
    return(average)

def get_most_watched_genre(user_data):
    genre_list = []
    popular_genre = ''
    if user_data["watched"] == []:
        return None

    else:
        for genre in user_data["watched"]:
            genre_list.append((genre["genre"]))
        popular_genre = max(genre_list, key = genre_list.count)
        return popular_genre   

#WAVE 3
def get_unique_list_of_users_movies(user_data):
    users_movies = []
    for movie in user_data["watched"]:
        if movie not in users_movies:
            users_movies.append(movie)
    return users_movies

def get_unique_list_of_friends_movies(user_data):
    friends_movies = []
    for friends_watched in user_data["friends"]:
        for movies_watched in friends_watched["watched"]:
            if movies_watched not in friends_movies:
                friends_movies.append(movies_watched)
    return friends_movies

def get_unique_watched(user_data): 
    users_movies = get_unique_list_of_users_movies(user_data)
    friends_movies = get_unique_list_of_friends_movies(user_data)
    users_unique_movies = []

    for movies in users_movies:
        if movies not in friends_movies:
            users_unique_movies.append(movies)
    return users_unique_movies

def get_friends_unique_watched(user_data): 
    users_movies = get_unique_list_of_users_movies(user_data)
    friends_movies = get_unique_list_of_friends_movies(user_data)
    friends_unique_list = []

    for movies in friends_movies:
        if movies not in users_movies:
            friends_unique_list.append(movies)
    return friends_unique_list

#WAVE 4
def get_available_recs(user_data):
    reccomendations = []
    for friend in user_data["friends"]:
        for friends_watched in friend["watched"]:
            if {"title":friends_watched["title"]} not in user_data["watched"]\
                and friends_watched["host"] in user_data["subscriptions"]:
                if friends_watched not in reccomendations:
                    reccomendations.append(friends_watched)
    return reccomendations

#WAVE 5
def get_new_rec_by_genre(user_data):
    frequent_genre = get_most_watched_genre(user_data)
    user_not_watched = get_friends_unique_watched(user_data)
    reccomendations = []

    for movie in user_not_watched:
        if movie["genre"] == frequent_genre:
            reccomendations.append(movie)
    
    return reccomendations

def get_rec_from_favorites(user_data):
    unique_recs = get_unique_watched(user_data)
    user_faves = user_data["favorites"]
    reccomendations =[]

    for movie in unique_recs: 
        if not user_faves:
            reccomendations
        if movie in user_faves: 
            reccomendations.append(movie)

    return reccomendations