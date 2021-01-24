#Wave 1

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