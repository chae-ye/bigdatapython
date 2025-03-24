import requests

# TMDb API 키 (자신의 API 키로 교체하세요)
api_key = "YOUR_TMDB_API_KEY"

# TMDb에서 넷플릭스 상영 영화 리스트 가져오기 (예시로 'now_playing' 필터 사용)
url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={api_key}&language=en-US&page=1"

# API 요청
response = requests.get(url)
data = response.json()

# 영화 리스트 추출
top_100_movies = []
for idx, movie in enumerate(data['results'][:100], 1):  # 상위 100개 영화
    title = movie['title']
    release_date = movie['release_date']
    top_100_movies.append({"Rank": idx, "Title": title, "Release Date": release_date})

# 결과 출력
for movie in top_100_movies:
    print(f"Rank {movie['Rank']}: {movie['Title']} ({movie['Release Date']})")
