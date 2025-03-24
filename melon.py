from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬 웹드라이버 경로 설정 (chromedriver 경로를 지정하세요)
driver_path = '/path/to/chromedriver'  # 예: C:/chromedriver/chromedriver.exe
driver = webdriver.Chrome(executable_path=driver_path)

# 멜론 탑100 페이지 열기
url = "https://www.melon.com/chart/index.htm"
driver.get(url)

# 페이지 로딩 대기 (자바스크립트로 동적 데이터 로딩을 기다림)
time.sleep(3)  # 필요한 대기 시간은 네트워크 상태에 따라 다를 수 있음

# 차트 항목들 찾기
songs = driver.find_elements(By.CSS_SELECTOR, '.wrap_song_info')

# 곡 제목과 아티스트 정보를 저장할 리스트
top_100 = []

# 곡 제목과 아티스트 추출
for song in songs:
    title = song.find_element(By.CSS_SELECTOR, '.ellipsis.rank01').text
    artist = song.find_element(By.CSS_SELECTOR, '.ellipsis.rank02').text
    top_100.append({"Title": title, "Artist": artist})

# 결과 출력
for idx, song in enumerate(top_100, 1):
    print(f"{idx}. {song['Title']} - {song['Artist']}")

# 브라우저 종료
driver.quit()
