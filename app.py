from pyfiglet import Figlet
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import playsound
import time
import shutil

def check():
    if os.path.isdir('source'):
        if os.path.isdir('source/audio'):
            if os.path.isfile('source/audio/a.mp3'):
                print("있음")
            else:
                print("없음")
                FileisNone("source/audio/a.mp3", True)
            if os.path.isfile('source/audio/amogus.mp3'):
                print("있음")
            else:
                print("없음1")
                FileisNone("source/audio/amogus.mp3", True)
            if os.path.isfile('source/audio/b.mp3'):
                print("있음")
            else:
                print("없음2")
                FileisNone("source/audio/b.mp3", True)
        else:
            print("source/audio폴더가 없습니다")
            FileisNone("source/audio", False)
    else:
        print("source폴더가 없습니다")
        FileisNone("source", False)


    if os.path.isfile("main.py") or os.path.isfile("main.exe"):
        print("main.py 있음")
    else:
        print("main.py 없음")
        FileisNone("main.py", True)
    if os.path.isfile("app.py") or os.path.isfile("app.exe"):
        print("app.py 있음")
    else:
        print("app.py 없음")
        FileisNone("app.py", True)

    if os.path.isfile("worlds.json"):
        print("json")
    else:
        FileisNone("worlds.json", True)
        

def FileisNone(name:str ,file:bool):
    os.system('cls')
    if file:
        print(f"{name}파일이 없습니다")
    else:
        print(f"{name}폴더가 없습니다")
    print("치명적 오류가 발생하여 프로그램을 종료합니다")
    print("프로그램을 깃허브에서 다운 받았는지 확인 하세요")
    input()
    exit



check()



def mainmenu():
    os.system('cls')
    f = Figlet(font='chunky', width=100)
    print("=" * 100)
    print(f.renderText('naver comment bot'))
    print("=" * 100)
    print("    1. 네이버 ID 로그인")
    print("    2. 시작")
    print("    3. 사용자 프로필 확인")
    print("    4. 사용자 프로필 삭제")
    return input("메뉴를 선택하세요: ")

def naver_login():
    print("만들 사용자 이름을 입력해주세요\n자동 로그인을 켜고 IP 보안을 꺼주세요")
    username = input(">_")

    options = Options()
    options.add_argument(f"user-data-dir=C:\\user_data\\{username}")
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    try:
        driver = webdriver.Chrome(options=options)
    except Exception as e:
        print(f"WebDriver를 시작하는 중 오류가 발생했습니다: {e}")
        return

    driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")
    print("로그인 후 프로그램을 재시작 해주세요")
    input()
    exit()

def start_bot():
    print("1번 메뉴에서 만든 사용자 이름을 입력해주세요")
    user = input()
    print("네이버 카페 게시글 링크를 입력하세요")
    link = input()
    print("댓글 개수를 입력해주세요")
    banbok = int(input())
    print("사용자 지정 JSON 파일 사용 (True / False)")
    jsonfilluse = input().lower() == 'true'

    # main 모듈의 cafe 함수가 실제로 존재하는지 확인 필요
    try:
        import main
        main.cafe(banbok, link, user, jsonfilluse)
    except ImportError:
        print("main 모듈을 찾을 수 없습니다.")
    except AttributeError:
        print("main 모듈에 cafe 함수를 찾을 수 없습니다.")

def show_profiles():
    path = r"C:\user_data"
    try:
        file_list = os.listdir(path)
        if not file_list:
            print("사용자 프로필이 없습니다.")
        else:
            print("사용자 프로필:")
            for file in file_list:
                print(file)
    except FileNotFoundError:
        print(f"경로를 찾을 수 없습니다: {path}")
    except Exception as e:
        print(f"파일 목록을 불러오는 중 오류가 발생했습니다: {e}")
    
    input("메인 메뉴로 돌아가려면 아무 키나 입력하세요...")

def amogus():
    print("""\n\
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣤⣤⣤⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡿⠛⠉⠙⠛⠛⠛⠛⠻⢿⣿⣷⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⠈⢻⣿⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣸⣿⡏⠀⠀⠀⣠⣶⣾⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿⣄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⢰⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⢿⣷⡄⠀
⠀⠀⣀⣤⣴⣶⣶⣿⡟⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⠀
⠀⢰⣿⡟⠋⠉⣹⣿⡇⠀⠀⠀⠘⣿⣿⣿⣿⣷⣦⣤⣤⣤⣶⣶⣶⣶⣿⣿⣿⠀
⠀⢸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⣸⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠉⠻⠿⣿⣿⣿⣿⡿⠿⠿⠛⢻⣿⡇⠀⠀
⠀⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣧⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⣿⣿⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀
⠀⢿⣿⡆⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠸⣿⣧⡀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠃⠀⠀
⠀⠀⠛⢿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⣰⣿⣿⣷⣶⣶⣶⣶⠶⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⣽⣿⡏⠁⠀⠀⢸⣿⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣿⣿⡇⠀⢹⣿⡆⠀⠀⠀⣸⣿⠇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣦⣄⣀⣠⣴⣿⣿⠁⠀⠈⠻⣿⣿⣿⣿⡿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⠿⠿⠿⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ """)
    
    playsound.playsound("./source/audio/amogus.mp3")
    i = 0
    a = 100
    while i < a:
        print("a")
        time.sleep(0.1)
        print("am")
        time.sleep(0.1)
        print("amo")
        time.sleep(0.1)
        print("amog")
        time.sleep(0.1)
        print("amogu")
        time.sleep(0.1)
        print("amogus")
        time.sleep(0.1)
        print("AMOGUS")
        print("amogus")
        time.sleep(0.1)
        print("amogu")
        time.sleep(0.1)
        print("amog")
        time.sleep(0.1)
        print("amo")
        time.sleep(0.1)
        print("am")
        time.sleep(0.1)
        print("a")
        time.sleep(0.1)
        print("")
        time.sleep(0.1)
        i += 0.5
    
    playsound.playsound("./source/audio/amogus.mp3") 
    exit()

def destroy_profile():
    path = r"C:\user_data"
    
    try:
        file_list = os.listdir(path)
    except FileNotFoundError:
        print(f"경로를 찾을 수 없습니다: {path}")
        input("아무 키나 입력하여 메인 메뉴로 돌아갑니다...")
        return
    except Exception as e:
        print(f"파일 목록을 불러오는 중 오류가 발생했습니다: {e}")
        input("아무 키나 입력하여 메인 메뉴로 돌아갑니다...")
        return

    if not file_list:
        print("삭제할 폴더가 없습니다.")
        input("아무 키나 입력하여 메인 메뉴로 돌아갑니다...")
        return

    print("폴더 리스트: ", file_list)
    print("삭제할 폴더의 이름을 정확히 입력 해주세요")
    folder_name = input()

    if folder_name in file_list:
        folder_path = os.path.join(path, folder_name)
        confirm = input(f"정말로 {folder_name} 폴더를 삭제하시겠습니까? 이 작업은 되돌릴 수 없습니다. (yes/no): ")
        if confirm.lower() == "yes":
            try:
                shutil.rmtree(folder_path)
                print(f"{folder_name} 폴더와 그 안의 모든 내용이 성공적으로 삭제되었습니다.")
            except Exception as e:
                print(f"폴더를 삭제하는 중 오류가 발생했습니다: {e}")
        else:
            print("삭제 작업이 취소되었습니다.")
    else:
        print("입력한 이름이 폴더 리스트에 없습니다. 다시 시도해주세요.")
    
    input("아무 키나 입력하여 메인 메뉴로 돌아갑니다...")

if __name__ == "__main__":
    while True:
        menu_selection = mainmenu()
        if menu_selection == "1":
            naver_login()
        elif menu_selection == "2":
            start_bot()
        elif menu_selection == "3":
            show_profiles()
        elif menu_selection == "4":
            destroy_profile()
        elif menu_selection == "amogus":
            amogus()
        else:
            print("잘못된 입력입니다. 다시 시도해주세요.")
