import requests
from bs4 import BeautifulSoup
import random

# 멜론 차트 페이지 URL
url = 'https://www.melon.com/chart/index.htm'  # 멜론의 최신 차트 URL로 확인 필요

# 헤더 설정 (멜론은 User-Agent 확인을 통해 봇 접근을 차단할 수 있으므로 설정이 필요할 수 있음)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}

# 웹페이지 요청
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 노래 제목과 아티스트를 담을 리스트
songs = []

# 멜론 차트의 노래 제목과 아티스트를 찾습니다.
#lst50 #frm > div > table > tbody #lst50
for entry in soup.select('tr.lst50, tr.lst100'):  # 상위 50위 및 100위 목록
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 수집한 데이터를 출력합니다.
for song in songs:
    print(f"{song[0]}. {song[1]} - {song[2]}")


# 멜론 차트 100 중에서 노래 한곡 추천 해주는 서비스 만들기
ai_song = random.choice(songs)
print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.") 


# 1. 멜론 100 추천
# 2. 멜론 50 추천
# 3. 멜론 10 추천
# 4. AI 추천 노래 출력
# 5. 가수 이름 검색
# 6. 1~5까지 입력하시오


print("=================")
print("1. 멜론 100 ")
print("2. 멜론 50 ")
print("3. 멜론 10 ")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("6. 1~5까지 입력하시오")
print("=================")

# 메뉴선택(입력): 1
n= input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")
# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
     print("멜론 100")
for i in range(100):
    print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 만약에 2를 입력하면 
# 멜론 50 출력
elif n== "2":
print("멜론 50")
for i in range(50):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 만약에 3을 입력하면
# 멜론 10 출력
elif n== "3":
print("멜론 10")
for i in range(10):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 만약에 4을 입력하면
# 멜론 AI 추천 노래 출력
elif n== "4":
print("AI 추천 노래")
ai_song = random.choice(songs)
print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.") 

# 5를 입력하면 가수이름을 검색할수있는 입력창 필요
# 이름을 입력하면 해당 가수이름의 노래가 출력
elif n== "5":
import requests
from bs4 import BeautifulSoup
import urllib.parse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def search_artist_and_get_songs(artist_name):
    search_url = "https://www.melon.com/search/song/index.htm"
    params = {
        "q": artist_name,
        "section": "artist",
        "searchGnbYn": "Y",
        "kkoSpl": "Y"
    }

    # 세션 사용 (멜론은 쿠키나 세션이 없으면 차단하기도 함)
    session = requests.Session()
    session.headers.update(headers)

    # Step 1: 검색 결과에서 아티스트 ID 추출
    search_response = session.get(search_url, params=params)
    if "로그인이 필요합니다" in search_response.text:
        print("❗ 멜론은 로그인 또는 우회가 필요할 수 있습니다.")
        return

    soup = BeautifulSoup(search_response.text, "html.parser")
    artist_section = soup.select_one("div.wrap_atist_info")

    if not artist_section:
        print(f"'{artist_name}'라는 가수를 멜론에서 찾을 수 없습니다.")
        return

    artist_link = artist_section.select_one("a.btn_atist")["href"]
    artist_id = artist_link.split("'")[1]

    # Step 2: 아티스트 페이지에서 인기곡 가져오기
    artist_url = f"https://www.melon.com/artist/song.htm?artistId={artist_id}"
    artist_response = session.get(artist_url)
    soup = BeautifulSoup(artist_response.text, "html.parser")

    song_tags = soup.select("div.ellipsis.rank01 a")
    songs = [tag.text.strip() for tag in song_tags]

    print(f"🎤 '{artist_name}'의 인기곡 목록 (멜론 기준):")
    for i, title in enumerate(songs, 1):
        print(f"{i}. {title}")

artist = input("가수 이름을 입력하세요: ")
search_artist_and_get_songs(artist)

 # 6을 입력하면 1~5까지 입력하시오를 출력
if n == "6":
    print("1~5까지 입력하시오")
n= input("메뉴선택(숫자입력): ")