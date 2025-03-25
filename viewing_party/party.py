# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # Check if all parameters are truthy (not empty, not None, etc.)
    if title and genre and rating:
        # Return a dictionary with the movie details
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    else:
        # Return None if any of the parameters are missing or falsy
        return None

def add_to_watched(user_data, movie):
    # Create a duplicate of user data 
    updated_data = user_data.copy()
    
    # Append the movie to the user's watched list
    updated_data["watched"].append(movie)
    
    # Return the updated user data
    return updated_data

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

