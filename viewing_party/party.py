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
    
    # Find movie in watchlist
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
    
    # Return user data
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
def get_unique_watched(user_data):
    # Get the user's watched list
    user_watched = user_data["watched"]

    # Create a list to hold all the movie titles friends have watched
    friends_titles = []

    # Go through each friend
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_titles:
                friends_titles.append(movie["title"])

    # Create a list for movies that only the user has watched
    unique_to_user = []

    for movie in user_watched:
        if movie["title"] not in friends_titles:
            unique_to_user.append(movie)

    return unique_to_user




def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    friends_unique_movies = []

    # Get titles of movies the user has already watched
    user_titles = [movie["title"] for movie in user_watched]

    # Go through each friend
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # Only add if the movie's title is not in the user's watched list
            # and it's not already in our result list
            if (
                movie["title"] not in user_titles
                and movie not in friends_unique_movies
            ):
                friends_unique_movies.append(movie)

    return friends_unique_movies



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    user_watched = user_data["watched"]
    user_subscriptions = user_data["subscriptions"]
    
    # check friends watched, subs, and current recs if no conficts add movie
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if (movie not in user_watched and 
                movie["host"] in user_subscriptions and 
                movie not in recommendations):
                recommendations.append(movie)
    
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    # Count how many times the user has watched each genre
    genre_count = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] = genre_count[genre] + 1
        else:
            genre_count[genre] = 1

    # If the user hasn't watched anything, there's nothing to base recs on
    if genre_count == {}:
        return []

    # Find the genre the user watches the most
    most_genre = None
    max_count = 0

    for genre in genre_count:
        if genre_count[genre] > max_count:
            most_genre = genre
            max_count = genre_count[genre]

    # Store all titles the user has watched to avoid recommending them again
    user_titles = []
    for movie in user_data["watched"]:
        user_titles.append(movie["title"])

    # Build recommendations list
    recs = []
    rec_titles = []  # Keep track of what we've already added

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            genre = movie["genre"]

            # Recommend only if it's the favorite genre, not watched, and not already in recs
            if title not in user_titles and genre == most_genre and title not in rec_titles:
                recs.append(movie)
                rec_titles.append(title)

    return recs


def get_rec_from_favorites(user_data):
    # Gather all the movie titles that friends have watched
    friends_titles = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if title not in friends_titles:
                friends_titles.append(title)

    # Recommend favorites only if none of the friends have watched them
    recs = []

    if "favorites" in user_data:
        for movie in user_data["favorites"]:
            title = movie["title"]
            if title not in friends_titles:
                recs.append(movie)

    return recs

