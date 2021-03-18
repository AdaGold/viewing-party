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
answer=create_movie("TitleA","Fantasy",4.8)
print(answer)

##2.
def add_to_watched(user_data,movie):
      user_data["watched"]=[]
      user_data["watched"].append(movie)
      return user_data
###3.
def add_to_watchlist(user_data,movie):
      user_data["watchlist"]=[]
      user_data["watchlist"].append(movie)
      return user_data
####4.
def watch_movie(user_data,title):
      for item in user_data["watchlist"]:
            # print(item)
            if  item["title"]==title:
                  user_data["watchlist"].remove(item)
                  user_data["watched"].append(item)
                        

                  
      return user_data
#wave2 
#1
def get_watched_avg_rating(user_data):
      sum=0
      average=0.0
     
      for item in user_data["watched"]:
            if len(user_data["watched"])!=0:
                  sum+=item["rating"]
                  average = sum/len(user_data["watched"])
      return average


##2
def get_most_watched_genre(user_data):
      my_dict={}
      if len(user_data["watched"])==0:
            return None
      for item in user_data["watched"]:
            if item["genre"] not in my_dict:
                  my_dict[item["genre"]] = 1
            else:
                  my_dict[item["genre"]] += 1
                  
      
      max_value=max(my_dict.values())
      max_keys=[k for k,v in my_dict.items() if v==max_value]
      return max_keys[0]
      # return max_value
      

#wave3
#1
def get_friends_movies(user_data):
      #given user_data, return a list of all the movies that my friends havewatched
      user_friend_movies_list=[]
      for friend in user_data["friends"]:
            for movie in friend["watched"]:
                  user_friend_movies_list.append(movie)
      return user_friend_movies_list


def get_unique_watched(user_data):
      friends_movies = get_friends_movies(user_data)
      movie_list=[]
      for user_movie_title in user_data["watched"]:
            # print(user_movie_title)  
            if user_movie_title not in  friends_movies :
                       movie_list.append(user_movie_title)                
      return movie_list
##2
 
def get_friends_unique_watched(user_data):
      friends_movies = get_friends_movies(user_data)
      movie_list_1=[i for n, i in enumerate(friends_movies) if i not in friends_movies[:n]]
      movie_list_2=[]
      for movie in movie_list_1:
            # print(user_movie_title)  
            if movie not in  user_data["watched"] :
                      movie_list_2.append(movie)               
      return movie_list_2
#wave4
#1
def get_available_recs(user_data):
      list_of_recommended_movies=[]
      for service_type in user_data["subscriptions"]:
            for friend in user_data["friends"]:
                  for movie in friend["watched"]:
                        if service_type== movie["host"]:
                           list_of_recommended_movies.append(movie)

      list_1=[i for n, i in enumerate(list_of_recommended_movies) if i not in list_of_recommended_movies[:n]]
      return list_1

#wave5
#1
def get_users_movies(user_data):
      #given user_data, return a list of all the movies that my friends havewatched
      users_movies_title_list=[]
      for movie in user_data["watched"]:
            movie_title=movie["title"]
            users_movies_title_list.append(movie_title)
      return users_movies_title_list
def get_new_rec_by_genre(user_data):
      recommended_movies_list=[]
      most_genre=get_most_watched_genre(user_data)
      user_titles=get_users_movies(user_data)
      for friend in user_data["friends"]:
                  for movie in friend["watched"]:
                        if movie["title"] not in user_titles and movie["genre"]==most_genre:
                              recommended_movies_list.append(movie)

                  
      return recommended_movies_list

#2
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
      