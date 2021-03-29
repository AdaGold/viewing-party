
# iterate through the lists of movies the user has watched
#user_data["watched"]

# if it's not in the friends list, append it to a new list

# iterate through users_data["friends"], we can create a list of the movies the friends has watched
# <-- create a list that's the movies all the friends have watched

friends_list = []
for watched_dict in user_data["friends"]:
    # some more nesting to pull out the friends' movies
    if friend_movie not in friends_list:
        friends_list.append(friend_movie)


movie_list = []
for user_movie in user_data["watched"]:
    if user_movie not in friends_list:
        movie_list.append(user_movie)