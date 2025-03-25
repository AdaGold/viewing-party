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

def add_to_watchlist(user_data, movie):
    # Create a duplicate of user data

    # Add movie to the user watchlist
    
    # Return user data
    pass



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def uses_available_letters(word, letter_bank):
    #make a list to count how many times  each letter appears in the letter bank 
    letter_counts = {}
    #count each letter in the bank 
    for letter in letter_bank:
        if letter in letter_counts:
            #increase letter counts by 1 
            letter_counts[letter] += 1
        else:
            #else set it equal to 1 
            letter_counts[letter] = 1

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

