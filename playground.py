all_genres = ['horror', 'comedy', 'indie', 'comedy']
max(set(all_genres), key=all_genres.count)

max = 0
max_genre = None

for genre in set(all_genres):
    count = 0
    for genre_item in all_genres:
        if genre_item == genre:
            count += 1
    if count > max:
        max = count
        max_genre = genre

print(max)
print(max_genre)