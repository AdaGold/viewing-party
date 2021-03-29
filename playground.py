from viewing_party.main import *

# Arrange
movie_title = "Title A"
genre = "Horror"
rating = 3.5

# Act
new_movie = create_movie(movie_title, genre, rating)

print(new_movie)