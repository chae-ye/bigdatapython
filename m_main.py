import func


# 사용자의 입력을 받아서 멜론 차트 출력 프로그램 만들기
# 각각 기능(함수)을 만들어서 메인 파일에서 코드 작성


# 만약에 a을 입력하면
# func.m100("멜론 100")
# 만약에 b를 입력하면
# func.m50("멜론 50")
# 만약에 c을 입력하면
# func.m10("멜론 10")
# 만약에 d를 입력하면
# func.m_random("노래추천 기능")
# 만약에 e를 입력하면
# 가수이름 검색 창
# 만약에 f을 입력하면
# 멜론 100을 파일에 저장
# 만약에 g을 입력하면
# func.m000("멜론 내맘대로 출력", 7)


import func

# 사용자의 입력을 받아서 멜론 차트 출력 프로그램 만들기
# 각각 기능(함수)을 만들어서 메인 파일에서 코드 작성

while True:
    print("\n=================")
    print("m100. 멜론 100")
    print("m50. 멜론 50")
    print("m10. 멜론 10")
    print("d. AI 추천 노래")
    print("e. 가수 이름 검색")
    print("f. 파일에 저장(멜론 100)")
    print("g. 원하는 만큼의 순위")
    print("x. 종료")
    print("=================")

    n = input("메뉴선택(알파벳 입력): ")
    print(f"\n당신이 입력한 값은: {n}\n")

    if n == 'm100':
        func.m100("멜론 100")
    
    elif n == 'b':
        func.m50("멜론 50")
    
    elif n == 'c':
        func.m10("멜론 10")
    
    elif n == 'd':
        func.m_random("노래추천 기능")
    
    elif n == 'e':
        singer = input("검색할 가수 이름을 입력하세요: ")
        func.search_singer(singer)
    
    elif n == 'f':
        func.save_to_file("melon100.txt")
    
    elif n == 'g':
        func.m000("멜론 내맘대로 출력")
    
    elif n == 'x':
        print("프로그램을 종료합니다.")
        break
    
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")