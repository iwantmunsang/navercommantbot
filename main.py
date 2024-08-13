from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import random
import playsound
import json

def cafe(a: int, b: str, c: str , d: str):
    print("자동화를 시작합니다...")
    
    options = Options()
    options.add_argument(r"user-data-dir=C:\\user_data\\"+c)  # 윈도우 경로를 위한 raw 문자열 사용 권장
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # 옵션을 사용하여 WebDriver 초기화
    driver = webdriver.Chrome(options=options)

    # URL로 이동
    driver.get(b)
    time.sleep(1)

    try:
        # 텍스트 영역이 포함된 프레임으로 전환
        driver.switch_to.frame("cafe_main")

        # 텍스트 영역 요소 찾기
        query = driver.find_element(By.TAG_NAME, "textarea")

        # 'd' 플래그에 따라 단어 리스트 로드
        if d:  # `d`가 True인 경우
            file_path = 'worlds.json'
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            words = data["단어"]
        else:  # `d`가 False인 경우
            # 랜덤 단어 리스트
            words = ["가", "나", "다", "라", "마", "바", "사", "아", "자", "차", "카", "파", "하",
                     "쀫", "뽰", "뽮", "짲", "얎", "뺪", "빲", "쫪", "괎", "꽚", "럆", "쓦", "썞",
                     "뽯", "왒", "왔", "얎"]
        i = 0
        error = 0
        while i < a:
            try:
                time.sleep(random.uniform(3, 4))  # 1초에서 4초 사이의 랜덤 지연
                random_word = random.choice(words)
                print(f"랜덤으로 선택된 단어: {random_word}")

                # 랜덤 단어를 텍스트 영역에 입력
                query.send_keys(random_word)
                

                # Ctrl+Enter를 눌러 댓글 제출
                query.send_keys(Keys.CONTROL, Keys.ENTER)
                
                i += 1  # 카운터 증가
                print(f"목표: {a}, 현재: {i}")
                if i == a:
                    playsound.playsound("./source/audio/a.mp3")
            except Exception as e:
                print(f"오류가 발생했습니다: {e}")
                error += 1
                if error >= 3:  # 연속 오류가 3번 이상 발생하면 중지
                    print("오류가 너무 많아 프로세스를 중지합니다.")
                    playsound.playsound("./source/audio/b.mp3")
                    break

    except Exception as e:
        print(f"프레임 전환 실패 또는 요소를 찾지 못했습니다: {e}")
        playsound.playsound("./b.mp3")
    finally:
        if i == None:
            print("치명적 오류로 프로세스가 종료되었습니다 프로그램을 다시 실행 하십시오")
            playsound.playsound("./source/audio/b.mp3")
        else:
            print(f"{i}번의 성공적인 작업과 {error}번의 오류로 프로세스가 완료되었습니다.")
            driver.quit()


# 사용 예시
# 
