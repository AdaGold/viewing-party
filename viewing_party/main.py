def create_movie(title, genre, rating):
    if (not title or not genre or not rating):
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating
    }

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# This was the most annoying function to write
def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        movie = user_data["watchlist"][i]
        if movie["title"] is title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
            break # TODO: write a test that fails if this is missing
    return user_data

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    sum = 0.0
    for movie in user_data["watched"]:
        sum += movie["rating"]
    return sum / len(user_data["watched"])

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    # Using a frequency map and counter approach:
    frequency_map = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if frequency_map.get(genre, 0):
            frequency_map[genre] += 1
        else:
            frequency_map[genre] = 1

    popular_genre = max(frequency_map)
    return popular_genre

def get_unique_watched(user_data):
    # Approach with multiple loops
    watched_movies = user_data["watched"]
    friends_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)

    unique_movies = []
    for movie in watched_movies:
        if movie not in friends_movies:
            unique_movies.append(movie)

    return unique_movies

# Is this implementation annoying?
def get_friends_unique_watched(user_data):
    watched_movies = user_data["watched"]
    unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in watched_movies and movie not in unique_movies:
                unique_movies.append(movie)

    return unique_movies

def get_available_recs(user_data):
    friend_recs = get_friends_unique_watched(user_data)
    recommendations = []

    for movie in friend_recs:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations


def get_new_rec_by_genre(user_data):
    movies = get_friends_unique_watched(user_data)
    genre = get_most_watched_genre(user_data)
    recs = []

    for movie in movies:
        if movie["genre"] is genre:
            recs.append(movie)

    return recs


def get_rec_from_favorites(user_data):
    options = get_unique_watched(user_data)
    recs = []

    for option in options:
        if option in user_data["favorites"]:
            recs.append(option)

    return recs
