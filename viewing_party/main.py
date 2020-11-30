def hw():
    return "Hello World"

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
            del user_data["watchlist"][i]
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

    # Using list comprehensions:
    # genres = [movie["genre"] for movie in user_data["watched"]]
    # return max(genres)
