import random

songs = ["a노래", "b노래", "c노래", "d노래"]
print (songs)
print(songs)
print(songs[0])
print(songs[1])
print(songs[2])
print(songs[3])

for songs in songs:
    print(songs)

print("노래추천해줘")
print("알겠습니다. 제가 분석한 곡을 추천드릴게요.")

ai_song = random.choice(songs)
print(f"제가 추천하는 곡은 {ai_song} 입니다.")

song1 = "a노래"
song2 = "b노래"
song3 = "c노래"
song4 = "d노래"

