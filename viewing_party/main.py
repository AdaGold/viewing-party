#Wave 1
#1.
def create_movie(movie_title, genre, rating):
      if movie_title!=None and genre!=None and rating!=None:
            new_movie={}
            new_movie["title"]=movie_title
            new_movie["genre"]=genre
            new_movie["rating"]=rating
            return new_movie
            
      return None
# answer=create_movie("TitleA","Fantasy",4.8)
# print(answer)

##2.
def add_to_watched(user_data,movie):
      if "watched" in user_data:
            user_data["watched"].append(movie)
      return user_data
###3.
def add_to_watchlist(user_data,movie):
      if "watchlist" in user_data:
            user_data["watchlist"].append(movie)
            return user_data
####4.
def watch_movie(user_data,title):
      for movie in user_data["watchlist"]:
            # print(item)
            if  movie["title"]==title:
                  user_data["watchlist"].remove(movie)
                  user_data["watched"].append(movie)
                  break
                        

                  
      return user_data
#wave2 
#1
def get_watched_avg_rating(user_data):
      sum=0
      for movie in user_data["watched"]:
            sum+=movie["rating"]
      if len(user_data["watched"])==0:
            return 0.0
      return sum/len(user_data["watched"])
##2
def get_most_watched_genre(user_data):
      numbers_movie_by_genre={}
      if len(user_data["watched"])==0:
            return None
      for movie in user_data["watched"]:
            if movie["genre"] not in numbers_movie_by_genre:
                  numbers_movie_by_genre[movie["genre"]] = 1
            else:
                  numbers_movie_by_genre[movie["genre"]] += 1
                  
      max_value=0
      most_watch_genre=""
      for movie_genre,watch_times in numbers_movie_by_genre.items():
            if watch_times > max_value:
                  max_value=watch_times
                  most_watch_genre=movie_genre
      return most_watch_genre
      

#wave3
#1
def get_friends_movies(user_data):
      #given user_data, return a list of all the movies that my friends havewatched
      user_friend_movies_list={}
      for friend in user_data["friends"]:
            for movie in friend["watched"]:
                  user_friend_movies_list[movie["title"]] = movie
      return user_friend_movies_list


def get_unique_watched(user_data):
      friends_movies = get_friends_movies(user_data)
      movie_list=[]
      for user_movie in user_data["watched"]:
            # print(user_movie_title)  
            if user_movie["title"] not in friends_movies:
                  movie_list.append(user_movie)                
      return movie_list
##2
def get_friends_unique_watched(user_data):
      user_movies_set=set()
      friends_movies = get_friends_movies(user_data)
      # friends_movies_no_repeated_list=[i for n, i in enumerate(friends_movies) if i not in friends_movies[:n]]
      # print(friends_movies_no_repeated_list)
      user_doesnt_watched_friends_watched_movie_list=[]
      for movie in user_data["watched"]:
            user_movies_set.add(movie["title"])
      for movie in friends_movies.values():
            # print(user_movie_title)  
            if movie["title"] not in user_movies_set:
                  
                  user_doesnt_watched_friends_watched_movie_list.append(movie)               
      return user_doesnt_watched_friends_watched_movie_list
#wave4
#1
def get_available_recs(user_data):
      list_of_recommended_movies=[]
      for service_type in user_data["subscriptions"]:
            for friend in user_data["friends"]:
                  for movie in friend["watched"]:
                        if service_type== movie["host"]:
                              list_of_recommended_movies.append(movie)

      list_of_recommended_movies_no_repeat=[i for n, i in enumerate(list_of_recommended_movies) if i not in list_of_recommended_movies[:n]]
      return list_of_recommended_movies_no_repeat

#wave5
#1
def get_users_movies(user_data):
      #given user_data, return a list of all the movies that my friends have watched
      users_movies_title_list=[]
      for movie in user_data["watched"]:
            movie_title=movie["title"]
            users_movies_title_list.append(movie_title)
      return users_movies_title_list
def get_new_rec_by_genre(user_data):
      recommended_movies_list=[]
      #call function from wave2 (2nd test funciton)
      most_genre=get_most_watched_genre(user_data)
      user_titles=get_users_movies(user_data)
      for friend in user_data["friends"]:
                  for movie in friend["watched"]:
                        if movie["title"] not in user_titles and movie["genre"]==most_genre:
                              recommended_movies_list.append(movie)
      return recommended_movies_list

#2
#from given user_data rerun all friends movies title in a list
def get_friends_watched_movies(user_data):
      friends_watched_movies_title_list=[]
      for friend in user_data["friends"]:
            # print(friend)
            for movie in friend["watched"]:
                  friends_watched_movies_title_list.append(movie["title"])      
      return friends_watched_movies_title_list
# answer=get_friends_watched_movies(user_data)
# print(answer)
def get_rec_from_favorites(user_data):
      recommended_movies_from_favs=[]
      friends_watched_movies=get_friends_watched_movies(user_data)
      print(friends_watched_movies)
      for user_fav_movie in user_data["favorites"]:
            # print(user_fav_movie)
            # print(friends_watched_movies)
            if user_fav_movie["title"] not in  friends_watched_movies:
                  print(user_fav_movie["title"] ,friends_watched_movies)
                  recommended_movies_from_favs.append(user_fav_movie)
      return recommended_movies_from_favs