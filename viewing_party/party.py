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
    avg_rating = 0

    if not user_data["watched"]:
        return avg_rating
    
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]
    avg_rating = avg_rating/len(user_data["watched"])

    return avg_rating

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genre_count={}
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        if current_genre not in genre_count.keys():
            genre_count[current_genre] = 1
        else:
            genre_count[current_genre] += 1
    most_popular =[]
    for genre, count in genre_count.items():
        if not most_popular or most_popular[1] < count:
            most_popular = [genre, count]
    return most_popular[0]


# ------------- WAVE 3 -------------------- #

def get_unique_watched(user_data):
    unique_movie_list = []
    
    for movie in user_data["watched"]:
        for friend in user_data["friends"]:
            if movie["title"] == friend["title"]:
                continue
            else:
                unique_movie_list.append(movie)
    return unique_movie_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# ------------- WAVE 5 -------------------- #
def get_new_rec_by_genre(user_data):
    recommendations = []
    if not user_data["watched"]:
        return recommendations
    for friend in user_data["friends"]:
        if not friend["watched"]:
            return recommendations
    
    # most_watched_genre = get_most_watched_genre(user_data["watched"])
    # friend_unique_watched = get_friends_unique_watched(user_data)

def get_rec_from_favorites(user_data):
    reccomendations = []
    if not user_data["favorites"]:
        return reccomendations
    elif not user_data["friends"]:
        reccomendations = user_data["favorites"]
        return reccomendations
    
    
    # neither of these are working but they are general idea of how I had need to keep working on it

    for movie in user_data["favorites"]:
        if movie["title"] not in user_data["friends"][0]["watched"]:
            reccomendations.append(movie["title"])
    return reccomendations

    # for i in range(len(user_data["favorites"])):
    #     if user_data["favorites"][i]["title"] not in user_data["friends"]["watched"]:
    #         reccomendations.append(user_data["favorites"][i])
    # return reccomendations