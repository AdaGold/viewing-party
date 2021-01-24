# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie =  {
            "title": title,
            "genre": genre,
            "rating": rating
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
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total = 0
    movies = user_data["watched"]
    n = len(movies)

    if n == 0:
        return 0

    for movie in movies:
        total += movie["rating"]

    return total/n

def calculate_genre_freq(user_data):
    # make genre frequency hash
    genre_freqs = {}
    movies = user_data["watched"]
    for movie in movies:
        genre = movie['genre']
        try:
            if genre_freqs[genre] != 0:
                genre_freqs[genre] += 1
        except: 
            genre_freqs[genre] = 1

    return genre_freqs

def get_most_watched_genre(user_data):
    
    
    movies = user_data["watched"]

    if movies == []:
        return None

    #call helper function to get frequencies
    genre_freqs = calculate_genre_freq(user_data)   
    print(genre_freqs)
    highest_freq = 0 

    # find most frequent
    for genre in genre_freqs:
        freq = genre_freqs[genre]
        if  freq > highest_freq:
            most_frequent = genre
            highest_freq = freq

    return most_frequent

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_movie_titles(user_data):
    friend_movie_titles = []

    #get friends movie titles
    for watched_dict in user_data['friends']:
        for movie in watched_dict['watched']:
            if movie['title'] not in friend_movie_titles:
                friend_movie_titles.append(movie['title'])

    return friend_movie_titles

def get_unique_watched(user_data):
    user_movies = user_data['watched']
    user_unique_movie_titles = []
    friend_movie_titles = get_friends_movie_titles(user_data)

    #check for unique titles
    for movie in user_movies:
        if movie['title'] not in friend_movie_titles:
            user_unique_movie_titles.append({'title': movie['title']})
    
    return user_unique_movie_titles


def get_friends_unique_watched(user_data):
    friend_movie_titles = get_friends_movie_titles(user_data)
    unique_friend_unique_movie_titles = []

    for title in friend_movie_titles:
        if {'title': title} not in user_data['watched']:
            unique_friend_unique_movie_titles.append({'title': title})

    return unique_friend_unique_movie_titles

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------