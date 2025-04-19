import requests
from bs4 import BeautifulSoup
import random
import csv

def search_artist_and_get_songs(artist_name):
    search_url = "https://www.melon.com/search/song/index.htm"
    params = {
        "q": artist_name,
        "section": "artist",
        "searchGnbYn": "Y",
        "kkoSpl": "Y"
        }

url = 'https://www.melon.com/chart/index.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 정보 수집
songs = []
for entry in soup.select('tr.lst50, tr.lst100'):
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))


def m100(a):
    print(a)
    for i in range(min(100, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

def m50(b):
    print(b)
    for i in range(min(50, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

def m10(c):
    print(c)
    for i in range(min(10, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

def m_random(d):
    print(d)
    ai_song = random.choice(songs)
    print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.")

def artist(e):
    print(e)
    artist = input("검색할 가수 이름을 입력하세요: ")
    search_artist_and_get_songs(artist)

def data(f):
    print(f)
    save_songs_to_csv(songs)

def save_songs_to_csv(songs, filename='songs.csv'):
    # 멜론 TOP 100 출력
    print("멜론 TOP 100")
    for i in range(min(100, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

    # 파일 열기 및 CSV 저장
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
        # 헤더 작성
        writer.writerow(['순위', '곡명', '아티스트'])
        
        # 데이터 작성
        for song in songs[:100]:
            writer.writerow(song)

# 함수 실행
save_songs_to_csv(songs)

def mind(g):
    print(g)
    def print_top_n_songs(songs):
        try:
        n = int(input("출력할 순위 개수를 입력하세요 (예: 10, 50, 100): "))
        print(f"\n멜론 TOP {n}")
        for i in range(min(n, len(songs))):
            print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
    except ValueError:
        print("⚠ 숫자만 입력해주세요!")
