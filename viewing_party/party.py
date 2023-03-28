# ------------- WAVE 1 --------------------
# git testing

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data
        
def watch_movie(user_data, title):
    user_data_copy = user_data.copy()
    
    for i in range(len(user_data_copy["watchlist"])):
        if title == user_data["watchlist"][i]["title"]:
            add_to_watched(user_data, user_data["watchlist"][i])
            

    # for k,v in user_data.items():
    #     for i in v:
    #         if i["title"] == title



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

