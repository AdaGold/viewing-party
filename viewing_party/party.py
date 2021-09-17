# WAVE 1
def create_movie(title, genre, rating):
    if bool(title) and bool(genre) and bool(rating):
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None



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
        print(user_data) 
    else:
        return user_data



#WAVE 2
def get_watched_avg_rating(user_data):
    sum = 0
    i = 0
    for rating in user_data["watched"]:
        if len(user_data["watched"]) > 0: 
            for i in range(len(user_data["watched"])):
                rating = user_data["watched"][i]["rating"]
                sum += rating
                i += 1
                average_rating = (sum / len(user_data["watched"]))
            return average_rating
    if len(user_data["watched"]) == 0:
        average_rating = 0.0
        return average_rating



def get_most_watched_genre(user_data):
    count_genre = []
    i = 0

    if len(user_data["watched"]) == 0:
        return None
    else:
        for i in range(len(user_data["watched"])):
            genre = user_data["watched"][i]["genre"]
            count_genre.append(genre)

        most_watched_genre = max(count_genre, key = count_genre.count)
        return most_watched_genre



#WAVE 3
def get_unique_watched(user_data):
    unique_user_watched = []
    friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in user_data["watched"]:
        if movie not in friends_watched:
            unique_user_watched.append(movie)
    return unique_user_watched



def get_friends_unique_watched(user_data):
    unique_friends_watched = []
    user_watched = []

    for movie in user_data["watched"]:
            user_watched.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]: 
            if movie not in user_watched:
                if movie not in unique_friends_watched: 
                    unique_friends_watched.append(movie)
    return unique_friends_watched



#WAVE 4
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    user_recommendations = []


    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            if movie not in user_recommendations:
                user_recommendations.append(movie)
    return user_recommendations



#WAVE 5
def get_new_rec_by_genre(user_data):
    user_most_watched_genre = get_most_watched_genre(user_data)
    user_recs_based_on_genre = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"]:
                if movie["genre"] == user_most_watched_genre:
                    if movie not in user_recs_based_on_genre:
                        user_recs_based_on_genre.append(movie)
    return user_recs_based_on_genre



def get_rec_from_favorites(user_data):
    friends_watched = []
    user_recs_from_favs = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            if movie not in user_recs_from_favs:
                user_recs_from_favs.append(movie)
    return user_recs_from_favs