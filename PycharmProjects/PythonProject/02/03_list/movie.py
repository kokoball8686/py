movies = {'파묘': [23.6, 5.5, 11914798],
          '범죄도시4': [20.6, 8.8, 11502779],
          '인사이드 아웃2': [15.6, 8.8, 7525302],
          '베테랑2': [10.8, 5.3, 5000000]}


# 파묘의 관객수는?

print(movies['파묘'][2])

# 평점이 8.8인 영화 제목은?

for movie in movies:
    # print(movie, movies[movie])
    if movies[movie][1] == 8.8:
        print(movie)

print("2")

# 관객수가 1000만명 이상 되는 영화 제목은?

for movie in movies:
    if movies[movie][2] > 10000000:
        print(movie)