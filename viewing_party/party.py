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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

