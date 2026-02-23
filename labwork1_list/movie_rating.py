ratings = [5, 4, 3, 6, 2, 5, 0]

# Remove invalid
ratings = [r for r in ratings if 1 <= r <= 5]

average = sum(ratings) / len(ratings)
five_star = ratings.count(5)

ratings.sort()

print("Average Rating: - movie_rating.py:11", average)
print("5Star Ratings: - movie_rating.py:12", five_star)
print("Sorted Ratings: - movie_rating.py:13", ratings)

#output:
# Average Rating: - movie_rating.py:11 3.5714285714285716
# 5Star Ratings: - movie_rating.py:12 2
# Sorted Ratings: - movie_rating.py:13 [2, 3, 4, 5, 5]