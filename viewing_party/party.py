# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    title_genre_rating = {}
    if title and genre and rating:
        title_genre_rating.update({'title': title, 'genre': genre, 'rating': rating})
        return(title_genre_rating)
    return None
    
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

    # user_data = {watched: [{movie}{moveie}]}
    # add each movie to the watched key

def add_to_watchlist(user_data, movie):
    # user_data = {watchlist: [{movies}{user}]{wants}{to_watch}}
    # add movie into the watchlist inside of user data
    # return user_data
    user_data["watchlist"].append(movie)
    return(user_data)


        

    # if truthy return a dictionary
    # dictionary contains 3 key-value pairs
    # return none if falsy

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

