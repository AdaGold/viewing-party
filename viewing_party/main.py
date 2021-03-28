
###################### WAVE 1 PASSED #########################
### Wave 1.1 (4 tests - PASSED) ###
def create_movie(movie_title, genre, rating):
    
    new_movie = {
        "title": movie_title,
        "genre": genre,
        "rating": rating,
    }       
    
    if new_movie["title"] == None:
        new_movie = None
    elif new_movie["genre"] == None:
        new_movie = None
    elif new_movie["rating"] == None:
        new_movie = None
    return new_movie

### Wave 1.2 (1 test PASSED) ###
def add_to_watched(user_data, movie):    
    # user_data is a dictionary key"watched": value lists title,genre,rating
    # updated_data is a list of dictionaries
    user_data["watched"].append(movie)
    return user_data

### Wave 1.3 (1 test PASSED) ###
def add_to_watchlist(user_data, movie): 
    user_data["watchlist"].append(movie)
    return user_data

### Wave 1.4 (3 tests PASSED) ###
def watch_movie(user_data, title):
    for i in user_data["watchlist"]:
        if i["title"] == title:
            user_data["watchlist"].remove(i)
            user_data["watched"].append(i)
    return user_data


###################### WAVE 2 PASSED #########################
### Wave 2.1 (2 tests) PASSED ###
def get_watched_avg_rating(user_data):
    watched_count = 0
    rating_sum = 0.0
    average = 0.0
    if user_data["watched"] == []:
        return average
    else:
        for i in user_data["watched"]:
            watched_count += 1
            rating_sum += i["rating"]
    average = rating_sum / watched_count
    return average

### Wave 2.2 (2 tests) ###
def get_most_watched_genre(user_data):
    popular_genre = " "
    user_genres = {}
    genre_sort = []

    if user_data["watched"] == []:
        popular_genre = None
        return popular_genre
    for i in user_data["watched"]:
        if i["genre"] in user_genres:
            user_genres[i["genre"]] += 1
        else:
            user_genres[i["genre"]] = 1
        # user_genres = {"Fanstasy": 2, "Intrigue": 3}
    genre_sort = sorted(user_genres)
    # sorted puts user_genres' keys in a list ordered from lowest to highest value
    # ...so ... genre_sort = ["Fantasy", "Intrigue"] 
    popular_genre = genre_sort[-1]
    # popular_genre = Intrigue
    return popular_genre

###################### WAVE 3 PASSED #########################
### Wave 3.1 (2 tests) PASSED ###
def unique_helper(user_data):
# this solution uses sets to modify the data
# ...specializes function for removing data that's irrelevant
    user_set = set()
    friend_set = set()

    for user_movies in user_data["watched"]:
        user_set.add(user_movies["title"]) 
        # now user_set has the values from user(amandas) movies
        # user_set = {'Title B', 'Title D', 'Title E', 'Title A', 'Title C'}
    for friend_items in user_data["friends"]:
        for movie in friend_items["watched"]:
            for title,val in movie.items():
                friend_set.add(val)
    return user_set, friend_set

def get_unique_watched(user_data):
# Return a list of dictionaries that represents list of movies
    # extra step to put the data back into a dictionary -refactor
    user_set, friend_set = unique_helper(user_data)
    unique2user = (user_set - friend_set)
    # unique2user = {'Title B', 'Title E'}
    users_unique_list = []
    for i in unique2user:
        unique_user_movies = {"title": None}
        unique_user_movies["title"] = i
        users_unique_list.append(unique_user_movies)
    # users_unique_list = [{'title': 'Title B'}, {'title': 'Title E'}]
    return users_unique_list

### Wave 3.2 (3 tests) PASSED ###
def get_friends_unique_watched(user_data):
    user_set, friend_set = unique_helper(user_data)
    # Determine which movies friends have watched, but the user has not watched.
    unique2friends = (friend_set - user_set)
    friends_unique_list = [] 
    for i in unique2friends:
        unique_friends_movies = {"title": None}
        unique_friends_movies["title"] = i
        friends_unique_list.append(unique_friends_movies)
    return friends_unique_list

###################### WAVE 4 PASSED #########################
### Wave 4.1 (2 tests) PASSED ###
def get_available_recs(user_data):
    recommendations = []
    user_subscriptions = user_data["subscriptions"]

    for collection in user_data["friends"]:
        for movie in collection["watched"]:
            if movie in recommendations:
                continue
            elif movie not in user_data["watched"] and movie["host"] in user_subscriptions:
                recommendations.append(movie)
    return recommendations
                

###################### WAVE 5 #########################
### Wave 5.1 (4 tests) PASSED ###
def get_new_rec_by_genre(user_data):
    recommend_by_genre = []

    popular_genre = get_most_watched_genre(user_data)
    # Intrigue

    if user_data["watched"] == []:
        recommend_by_genre = user_data["watched"]
    else:   
        for account in user_data["friends"]:
            for movie in account["watched"]:
                if popular_genre in movie["genre"]:
                    recommend_by_genre.append(movie)

    return recommend_by_genre


### Wave 5.2 (1 test) PASSED ###
def get_rec_from_favorites(user_data):
    recommend_by_fav = []
    favorites = []
    friends_watched = []

    for film in user_data["favorites"]:
        favorites.append(film)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for seen in friends_watched:
        if seen in favorites:
            favorites.remove(seen)
            recommend_by_fav = favorites
                
    return(recommend_by_fav)