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
def get_unique_watched(user_data):
      movie_list=[]
      # if len(user_data["watched"])==0:
      #       return None
      
      for item_1 in user_data["watched"]:
            for item_2 in user_data["friends"]:
                  if item_1 not in item_2["watched"]:
                        movie_list.append(item_1)
      return movie_list


      