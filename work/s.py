# Bob has a playlist of songs, each song has a singer associated with it (denoted by an integer) Favourite singer of Bob is the one whose songs are the most on the playlist Count the number of Favourite Singers of Bob
from collections import Counter

n = int(input())

singers = list(map(int, input().split()))

singer_counts = Counter(singers)

max_count = max(singer_counts.values())

num_favorites = sum(count == max_count for count in singer_counts.values())

print(num_favorites)