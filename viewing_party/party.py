# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #returns None if a parameter is missing
    #else creates a dictionary for a movie. Includes three keys: title, genre, and rating
    #return movie

    if title == None or genre == None or rating == None:
        return None
    else:
        movie = {"title" : title,
                    "genre" : genre,
                    "rating" : rating,
                    }

    return movie

def add_to_watched(user_data, movie):
    #user_data is a dictionary that contains two key value pairs. The keys are "watched" and "watchlist." The values are lists that contain movies stored as dictionaries.
    #movie is a dictionary created with create_movie function
    #adds a movie into the list of movies paired with the "watched" key in user_data
    #return updated user_data

    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    #user_data is a dictionary that contains two key value pairs. The keys are "watched" and "watchlist." The values are lists that contain movies stored as dictionaries.
    #movie is a dictionary created with create_movie function
    #adds a movie into the list of movies paired with the "watchlist" key in user_data
    #return updated user_data

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    #user_data is a dictionary that contains two key value pairs. The keys are "watched" and "watchlist." The values are lists that contain movies stored as dictionaries.
    #movie_title is the value paired with the "title" key in a movie dictionary created with create_movie function
    #moves a movie dictionary with a title of movie_title from watch list in user_data to watched. 
    #return updated user_data

    for item in user_data["watchlist"]:
        if item["title"] == movie_title:
            user_data["watched"].append(item)
            user_data["watchlist"].remove(item)
        
    return user_data

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

