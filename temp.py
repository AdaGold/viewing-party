def calculate_genre_freq(user_data):
    #dictionary where the keys are the genre e.g. "fantasy"
    #go through watch list and check if it's in
    #if it's already in dictionary, add 1 to it

    # build a frequency map 
    # {
    # "Intrigue": 3, 
    # "Fantasy": 2
    # "Comedy": 5, 
    # "Horrr": 2
    # }
    #dictionary where the keys are the genre e.g. "fantasy"
    genre_freq_dict = {}
        watch_list = user_data["watched"]
        for movie in watch_list:
            genre = movie["genres"]
            #go through watch list and check if that genre is already a key 
            #if it's already in dictionary, add 1 to it
            if genre in genre_freq_dict.keys():
                genre_freq_dict[genre] += 1
            #otherwise we'll make an entry and give a value of 1
            else:
                genre_freq_dict[genre] = 1

        return genre_freq_dict

def get_most_watched_genre(user_data):
    # call calculate_genre_freq to get genre_freq_dict
    # initalize highest to 0
    # iterate through the genre_freq_dict
    # check if the value  (genre_freq_dict[genre]) is higher than the current value stored in highest
        # if it is assign highest_genre to current genre
        # and replace highest with the freq

    # return highest_genre