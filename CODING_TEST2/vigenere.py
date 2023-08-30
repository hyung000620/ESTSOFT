from selenium import webdriver
import time
"""
1. selenium 활용
2. https://www.guballa.de/vigenere-solver 에 접속
3.  textarea 에 id값이 cipher인 값에 내가 입력한 text 정보 넣기
4. input 에 id값이 keylength 인 값에 내가 입력한 key 값 넣기
5. <div class="button-wrapper"> 하위에 <button type="submit">
6. 1초 기다리기
7.  textarea name="cleartext" 값 가져와서 출력
"""
# Selenium 웹 드라이버 초기화
driver = webdriver.Chrome()  # Chrome 드라이버 사용. 다른 브라우저를 사용하려면 해당 브라우저의 드라이버를 설치해야 합니다.

try:
    # https://www.guballa.de/vigenere-solver 사이트 접속
    driver.get("https://www.guballa.de/vigenere-solver")

    # textarea에 입력할 text와 key 설정
    input_text = "O Hsx bbg hal grmeq o diahhkjuy pwrcu ch vics ivacsu laaukrg sfqq a iwpi teokreq onsnt hji beopghrg qj a gfgi. Tus ivacsu weragh rrofc tb pwvsg kkxh wikge, nbf xhr Tqb's zcwxh jovirrr cw hr ucdeq zqrgvbipy nh vlez. Hji bhbel hhbi jrba c litv dvaaqj, enq hji Fbl jed gc lymc tqv ig. Hji fvfux tvag le wioteq vg qifggh ig pa e lbbi aal. Gq le jonoeq chj a fvqvt qwuxaaqg enq hqsk n fwrnvbi pend cx ig, cppy gc hely gjsrg cpge zcti. Atokr aar ckavb ji tewgh, bhh kr vnwp. Roj vg wag rqan nbf pobygh ag hji georis vb fmstiux. \"Wuov e fbcn M az,\" vg wavr. \"Jirr W cq wrotmnt aaweyt qyt gc iit n pwrcu ch wohf ivacsu xhnh cve acv aoehj kacwpk fbf.\" Crd bth le jonoeq jgvy, istc spctrfhznc."
    key = "5"

    # textarea와 input 요소에 값을 입력
    cipher_input = driver.find_element("id", "cipher")
    cipher_input.clear()
    cipher_input.send_keys(input_text)

    key_length_input = driver.find_element("id", "keylength")
    key_length_input.clear()
    key_length_input.send_keys(key)

    # Submit 버튼 클릭
    submit_button = driver.find_element("css selector", ".button-wrapper button[type='submit']")
    submit_button.click()

    # 1초 대기
    time.sleep(1)

    # 결과 출력
    cleartext_output = driver.find_element("name", "cleartext").text
    print("복호화된 결과:", cleartext_output)

except Exception as e:
    print("오류 발생:", e)

finally:
    # 작업 완료 후 브라우저 닫기
    driver.quit()