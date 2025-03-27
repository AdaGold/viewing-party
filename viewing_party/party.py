# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # Check if all parameters are truthy (not empty, not None, etc.)
    if title and genre and rating:
        # Return a dictionary with the movie details
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    else:
        # Return None if any of the parameters are missing or falsy
        return None

def add_to_watched(user_data, movie):
    # Create a duplicate of user data 
    updated_data = user_data.copy()
    # Append the movie to the user's watched list
    updated_data["watched"].append(movie)
    # Return the updated user data
    return updated_data

def add_to_watchlist(user_data, movie):
    # Create a duplicate of user data
    updated_data = user_data.copy()
    # Add movie to the user watchlist
    updated_data["watchlist"].append(movie)
    # Return user data
    return updated_data


def watch_movie(user_data, movie_title):
    # Create a duplicate of user data
    updated_data = user_data.copy()
    
    # Find movie in watchlist by title
    movie_to_watch = None
    for movie in updated_data["watchlist"]:
        if movie["title"] == movie_title:
            movie_to_watch = movie
            break
    
    # If movie found in watchlist, move it to watched
    if movie_to_watch:
        # Remove movie from watchlist
        updated_data["watchlist"].remove(movie_to_watch)
        # Add movie to watched
        updated_data["watched"].append(movie_to_watch)
    
    # Return updated user data
    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # Grab the list of watched movies
    watched = user_data["watched"]

    # If they haven't watched any movies, return 0.0
    if len(watched) == 0:
        return 0.0

    # Add up all the ratings
    total_rating = 0
    for movie in watched:
        total_rating += movie["rating"]

    # Divide the total rating by how many movies they watched
    average = total_rating / len(watched)
    return average

def get_most_watched_genre(user_data):
    # grab list of most watched genre 
    watched = user_data["watched"]
    if len(watched) == 0:
        return None 
    #track how many times each genre comes up 
    genre_counts = {}
    #go through each move in the list 
    for movie in watched:
        genre = movie["genre"]
        #if the movie is already in dict add 1 
        if genre in genre_counts: 
            genre_counts[genre] += 1
            # if not in dict start at 1 
        else:
            genre_counts[genre] = 1 
    #store genre we see the most
    most_watched = None
    highest_count = 0
#look through all genres we counted
    for genre in genre_counts:
        #if the genre's count is bigger than what is current
        if genre_counts[genre] > highest_count:
            #update the most watched genre
            most_watched = genre
            #update its count
            highest_count = genre_counts[genre]

    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

