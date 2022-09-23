# ------------- WAVE 1 --------------------

from logging.handlers import TimedRotatingFileHandler
from statistics import mean, mode

def create_movie(title, genre, rating):
    movie = {'title': title, 'genre': genre, 'rating': rating}
    return None if None in {title, genre, rating} else movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watched'].append(movie)
            user_data['watchlist'].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = [movie['rating'] for movie in user_data['watched']]
    return 0.0 if not ratings else mean(ratings)

def get_most_watched_genre(user_data):
    genres = [movie['genre'] for movie in user_data['watched']]
    return None if not genres else mode(genres) 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# supporting function to return movies watched friends
def friends_movies(user_data):
    friends_watched = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friends_watched:
                friends_watched.append(movie)
    return friends_watched

def get_unique_watched(user_data):
    friends_watched = friends_movies(user_data)
    unique_watched = []
    for movie in user_data['watched']:
        if movie not in friends_watched:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    friends_watched = friends_movies(user_data)
    friends_unique_watched = []
    for movie in friends_watched:
        if movie not in user_data['watched']:
            friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_watched = friends_movies(user_data)
    recommendations = []
    for movie in friends_watched:
        if movie not in user_data['watched'] and movie['host'] in user_data['subscriptions']:
            recommendations.append(movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friends_watched = friends_movies(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    recommendations = []
    for movie in friends_watched:
        if movie['genre'] == favorite_genre and movie not in user_data['watched']:
            recommendations.append(movie)
    return recommendations

def get_rec_from_favorites(user_data):
    friends_watched = friends_movies(user_data)
    recommendations = []
    for movie in user_data['favorites']:
        if movie not in friends_watched:
            recommendations.append(movie)
    return recommendations