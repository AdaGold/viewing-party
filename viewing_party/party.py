from statistics import mean, mode
# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
# If valid, creates a movie with title, genre, and rating as values of a dict
def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        movie = {"title" : title, "genre" : genre, "rating" : rating}
    return movie

# Adds movie dictionary to watched
def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data

# Adds movie dictionary to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# If the title is in a movie in the user's watchlist: remove that movie from the watchlist, add that movie to watched
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for film in range(len(watchlist)):
        if watchlist[film]["title"] == title:
            user_data["watched"].append(watchlist[film])
            del watchlist[film]
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Find and return avg of reviews in watched
def get_watched_avg_rating(user_data):
    reviews = []
    for film in user_data["watched"]:
        reviews.append(film["rating"])
    if not reviews:
        return 0
    average = mean(reviews)
    return average

# Find most frequently watched genre in watched list
def get_most_watched_genre(user_data):       
    genres = []
    for film in user_data["watched"]:
        genres.append(film["genre"])
    if not genres:
        return None
    frequency = mode(genres)
    return frequency

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Compiles info on movies friends have watched into a list
def get_friend_data(user_data):
  friends = []
  for data in user_data["friends"]:
    for each in data["watched"]:
      if each not in friends:
        friends.append(each)
  return friends

# Compiles info on movies user has watched into a list
def get_user_data(user_data):
  self = []
  for data in user_data["watched"]:
    if data not in self:
      self.append(data)
  return self

# Gets movies user has watched but friends haven't. Includes if ratings are different.
def get_unique_watched(user_data):
  unique = []
  friends = get_friend_data(user_data)
  user = get_user_data(user_data)
  for movie in user:
    if movie not in friends:
      unique.append(movie)
  return unique

# Gets movies friends have watched that user hasn't. Includes if ratings are different.
def get_friends_unique_watched(user_data):
  unique = []
  friends = get_friend_data(user_data)
  user = get_user_data(user_data)
  for movie in friends:
    if movie not in user:
      unique.append(movie)
  return unique


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# Returns list of recommendations (movies user hasn't watched but is able to watch, but >1 friend watched) 
def get_available_recs(user_data):
  recs = []
  friends = get_friend_data(user_data)
  user = get_user_data(user_data)
  for movie in friends:
    if movie not in user:
      if movie["host"] in user_data["subscriptions"]:
        recs.append(movie)
  return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Uses fave genre to find user-unwatched rec from friends list of watched
def get_new_rec_by_genre(user_data):
  recs = []
  user = get_user_data(user_data)
  friends = get_friend_data(user_data)
  fave = get_most_watched_genre(user_data)
  for movie in friends:
    if movie not in user and movie["genre"] == fave:
      recs.append(movie)
  return recs

# Recommends movies from user's fav list that no friends have watched
def get_rec_from_favorites(user_data):
  recs = []
  friends = get_friend_data(user_data)
  fave = user_data["favorites"]
  for each in fave:
    if each not in friends:
      recs.append(each)
  return recs


