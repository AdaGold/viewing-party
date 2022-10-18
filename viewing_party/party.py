# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    # if truthy return a dictionary
    # dictionary contains 3 key-value pairs
    # return none if falsy
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

def watch_movie(user_data, title):
#     user_data = {watchlist: watched:}
#     if title is in watch_list then add to watched:
#         return user_data
#     if not in watch list:
#         return user_data

    for movie in user_data["watchlist"]:
        if title in movie.values():
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return(user_data)



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
#  user data = {watched: [{movie2}, {movie2}]}
    user_rating = []
    
    if len(user_data["watched"]) == 0:
        average_rating = 0.0
        return average_rating
    else:
        for movie in user_data["watched"]:
            user_rating.append(movie["rating"])
            average_rating = (sum(user_rating)) / (len(user_rating))
    # print(user_rating)
    # print(average_rating)
        return(average_rating)

def get_most_watched_genre(user_data):
    
    genres_watched = {}

    if not user_data["watched"]:
        return None
    
    for movie in user_data["watched"]:
        if movie["genre"] not in genres_watched:
            genres_watched[movie["genre"]] = 1
        elif movie["genre"] in genres_watched:
            genres_watched[movie["genre"]] += 1
    
    num_of_genres_watched = genres_watched.values()
    max_num_genres_watched = max(num_of_genres_watched)

    for genre, times_watched in genres_watched.items():
        if times_watched == max_num_genres_watched:
            return genre
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    #  user_data = {watched :[{"title: title"}, {"title": title}], friends: [{watched_key:[{"title:title"}{title:title}]}{watched_key:[{title:title}{title:title}]}]}
    # each movie dict in watched_key has a title

    unique_movies = []
    movies_watched_by_friends = []
    
    for friend in user_data["friends"]:
        for movie_details in friend["watched"]:
            movie_title = movie_details["title"]
            movies_watched_by_friends.append(movie_title)
            # print(movie_details["title"])
    for movie in user_data["watched"]:
        movie_watched = movie["title"]
        if movie_watched not in movies_watched_by_friends:
            unique_movies.append(movie)
            # watched_titles.append(movie["title"])
    return(unique_movies)

def get_friends_unique_watched(user_data):
    all_movies_watched = []
    unique_movies_watched_by_friends = []
    
    for movie in user_data["watched"]:
        movie_watched = movie["title"]
        # add all the movies watched to new list
        all_movies_watched.append(movie_watched)
    for friend in user_data["friends"]:
        for movie_details in friend["watched"]:
            movie_title = movie_details["title"]
            if (movie_title not in all_movies_watched and 
                movie_details not in unique_movies_watched_by_friends):
                # check if details are unqie friends list to avoid duplicates
                # create list of dictionary containing movie details
                unique_movies_watched_by_friends.append(movie_details)
    return unique_movies_watched_by_friends
        

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)
    for movie in friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
