import requests
from bs4 import BeautifulSoup
import random
import csv



# 멜론 차트 페이지 URL
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

# 아티스트 검색 함수
def search_artist_and_get_songs(artist_name):
    search_url = "https://www.melon.com/search/song/index.htm"
    params = {
        "q": artist_name,
        "section": "artist",
        "searchGnbYn": "Y",
        "kkoSpl": "Y"
    }

    session = requests.Session()
    session.headers.update(headers)

    search_response = session.get(search_url, params=params)
    if "로그인이 필요합니다" in search_response.text:
        print("멜론은 로그인 또는 우회가 필요할 수 있습니다.")
        return

    soup = BeautifulSoup(search_response.text, "html.parser")
    artist_section = soup.select_one("div.wrap_atist_info")

    if not artist_section:
        print(f"'{artist_name}'라는 가수를 멜론에서 찾을 수 없습니다.")
        return

    artist_link = artist_section.select_one("a.btn_atist")["href"]
    artist_id = artist_link.split("'")[1]

    artist_url = f"https://www.melon.com/artist/song.htm?artistId={artist_id}"
    artist_response = session.get(artist_url)
    soup = BeautifulSoup(artist_response.text, "html.parser")

    song_tags = soup.select("div.ellipsis.rank01 a")
    songs = [tag.text.strip() for tag in song_tags]

    print(f"\n'{artist_name}'의 인기곡 목록:")
    for i, title in enumerate(songs, 1):
        print(f"{i}. {title}")

n = input("메뉴선택(알파벳입력): ")
print(f"\n당신이 입력한 것은: {n}\n")

# 멜론 100
def m100(title, songs):
    print(title)
    for i in range(min(100, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 멜론 50
def m50(title, songs):
    print(title)
    for i in range(min(50, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 멜론 10
def m10(title, songs):
    print(title)
    for i in range(min(10, len(songs))):
        print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# AI 추천
def m_random(title, songs):
    print(title)
    ai_song = random.choice(songs)
    print(f"🎵 추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.")

# 순위 직접 입력
def m000(title, songs):
    print(title)
    try:
        n = int(input("출력할 순위 개수를 입력하세요 (예: 10, 50, 100): "))
        for i in range(min(n, len(songs))):
            print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")
    except ValueError:
        print("⚠ 숫자만 입력해주세요!")

# 가수 검색 (미완성)
def search_singer(name):
    print(f"🔍 '{name}' 가수의 곡을 찾는 기능은 아직 준비 중입니다.")

# 파일 저장
def save_to_file(filename, songs):
    print("💾 멜론 100 데이터를 저장합니다.")
    with open(filename, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['순위', '곡명', '아티스트'])
        for song in songs[:100]:
            writer.writerow(song)