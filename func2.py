import func
from func import songs

def main():
    while True:
        print("\n=================")
        print("a. 멜론 100")
        print("b. 멜론 50")
        print("c. 멜론 10")
        print("d. AI 추천 노래")
        print("e. 가수 이름 검색")
        print("f. 파일에 저장(멜론 100)")
        print("g. 원하는 만큼의 순위")
        print("=================")

        choice = input("원하는 메뉴를 선택하세요: ").lower()

        if choice == 'a':
            func.m100("멜론 100")
        elif choice == 'b':
            func.m50("멜론 50")
        elif choice == 'c':
            func.m10("멜론 10")
        elif choice == 'd':
            func.m_random("노래추천 기능")
        elif choice == 'e':
            name = input("가수 이름을 입력하세요: ")
            func.search_artist(name)
        elif choice == 'f':
            func.save_m100_to_file("melon_100.txt")
        elif choice == 'g':
            try:
                num = int(input("몇 개의 순위를 출력할까요? (예: 7): "))
                func.m000("멜론 내맘대로 출력", num)
            except ValueError:
                print("숫자를 입력해주세요.")
        else:
            print("올바른 메뉴를 선택해주세요.")

if __name__ == "__main__":
    main()
