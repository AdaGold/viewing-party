# ------------- WAVE 1 -------------------- #

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    new_movie = {}

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            return user_data
    return user_data

# ------------- WAVE 2 -------------------- #

def get_watched_avg_rating(user_data):
    rating_sum = 0
    avg_rating = 0
    if not user_data["watched"]:
        return avg_rating
    
    for movie in user_data["watched"]:
        rating_sum += movie["rating"]
    avg_rating = rating_sum/len(user_data["watched"])

    return avg_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_count={}
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        current_genre_count = genre_count.get(current_genre, 0)
        genre_count[current_genre] = current_genre_count + 1
    most_popular =[]
    for genre, count in genre_count.items():
        if not most_popular or most_popular[1] < count:
            most_popular = [genre, count]
    return most_popular[0]

# ------------- WAVE 3 -------------------- #

def get_unique_watched(user_data):
    unique_movie_list = user_data["watched"].copy()
    removal_list = []
    for friend in user_data["friends"]:
        friend_movie_list = friend["watched"]
        for user_movie in unique_movie_list:
            if user_movie in friend_movie_list:
                removal_list.append(user_movie)
    for movie in removal_list:
        if movie in unique_movie_list:
            unique_movie_list.remove(movie)
    return unique_movie_list

def get_friends_unique_watched(user_data):
    user_movie_list = user_data["watched"].copy()
    friend_unique_list = []
    for friend in user_data["friends"]:
        friend_movie_list = friend["watched"]
        for friend_movie in friend_movie_list:
            if friend_movie not in user_movie_list and friend_movie not in friend_unique_list:
                friend_unique_list.append(friend_movie)
    return friend_unique_list

# ------------- WAVE 4 -------------------- #

def get_available_recs(user_data):
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"] and movie not in recommendations:
                recommendations.append(movie)
    return recommendations

# ------------- WAVE 5 -------------------- #

def get_new_rec_by_genre(user_data):
    recommendations = []
    if not user_data["watched"] or not user_data["friends"]:
        return recommendations
        
    most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_watched = get_friends_unique_watched(user_data)

    for movie in friend_unique_watched:
        if movie["genre"] == most_watched_genre:
            recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    if not user_data["favorites"]:
        return recommendations
    elif not user_data["friends"]:
        recommendations = user_data["favorites"]
        return recommendations
    else:
        for movie in user_data["favorites"]:
            for friend in user_data["friends"]:
                if movie in friend["watched"] and movie in recommendations:
                    recommendations.remove(movie)
                elif movie not in friend["watched"] and movie not in recommendations:
                    recommendations.append(movie)
    return recommendations