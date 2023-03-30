# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating: 
        return None
    if title and genre and rating:
        movie_dict = {}
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating

        return movie_dict

    
def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie_dict in user_data['watchlist']:
        if title == movie_dict['title']:
            user_data['watched'].append(movie_dict)
            user_data['watchlist'].remove(movie_dict)

    return user_data

    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0.0
    avg_rating = 0.0
    for movie_dict in user_data['watched']:
        total_rating += movie_dict['rating']
        if not len(user_data['watched']):
            avg_rating = 0.0
        else:
            avg_rating = total_rating / len(user_data['watched'])
    return avg_rating
            



def get_most_watched_genre(user_data):
    genre_count = {}
    if user_data['watched'] == []:
        return None
    for movie_dict in user_data['watched']:
        current_genre = movie_dict['genre']
        if current_genre not in genre_count:
            genre_count[current_genre] = 1
        else:
            genre_count[current_genre] += 1
    genre_most_watched = max(genre_count, key = genre_count.get)
    return genre_most_watched
    
    
        
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_movies(user_data):
    friends_movies = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_movies.append(movie)
    return friends_movies


def get_unique_watched(user_data):
    unique_movies = []
    friends_movies = get_friends_movies(user_data)
    for movie_dict in user_data['watched']:
        if movie_dict not in friends_movies:
            unique_movies.append(movie_dict)
    return unique_movies

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_unique_movies = []
    index = 0
    for movies_dict in user_data['watched']:
        user_watched_list.append(movies_dict['title'])

    for friends_dict in user_data['friends']:
        movie_list = friends_dict['watched']
        for movies_dict in movie_list:
            if movies_dict in friends_unique_movies:
                continue
            if movies_dict['title'] not in user_watched_list:
                friends_unique_movies.append(movies_dict)
    return friends_unique_movies

    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_movies = get_friends_unique_watched(user_data)
    subscriptions = user_data['subscriptions']
    reccomendations = []

    for movie_dict in friends_movies:
        if movie_dict['host'] in subscriptions:
            reccomendations.append(movie_dict)
    return reccomendations



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie['genre'] == most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies



def get_rec_from_favorites(user_data):
    user_favorites = user_data['favorites'] #list of dictionaries
    rec_favorites = []
    friends_watched = []
    for friends_dict in user_data['friends']: 
        movies_list = friends_dict['watched'] #list of dictionary movies
        for movies in movies_list:
            friends_watched.append(movies)

    for favorite_movie in user_favorites:
        if favorite_movie in rec_favorites:
            continue
        if favorite_movie not in friends_watched:
            rec_favorites.append(favorite_movie)

    return rec_favorites