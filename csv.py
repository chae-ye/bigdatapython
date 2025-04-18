#csv
import csv

# CSV 파일 쓰기
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    # 헤더 작성
    csv_writer.writerow(['순위', '제목', '가수'])
    # 데이터 행 작성
    csv_writer.writerow(['1', 30, 'New York'])
    csv_writer.writerow(['2', 25, 'Los Angeles'])
