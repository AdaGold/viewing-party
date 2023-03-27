# ------------- WAVE 1 --------------------

"""
    first function create movie
    function takes 3 paramaters/attributes, titles, genre, rating
    if three attributers are truthy, return dictionary
    if title falsy, genre is falsy or rating is falsy, these should return none
    
"""

def create_movie(title, genre, rating):
    
    #possible us of isinstance method
    #not accounting for opposite condition of none
    new_movie = {}

    if title or genre != str:
        return None
    if rating != int:
        return None
        
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

    return new_movie
    print(new_movie)
    


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

