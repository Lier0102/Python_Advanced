# 간단히 기능들을 사용해 보며 requests 모듈과 친숙해지기.

import requests

req = requests.get("https://google.com") # google에서 요청에 대한 응답을 받아옴

if req.status_code == 200:
    print("서버가 이상한디요.")

print(req.text) # get한 값들을 보여줌.

if req.text.find('body') != -1: # get 한 곳에서 body 태그 검사.
    print("<body> 태그가 존재합니다.")
    print(req.text[req.text.find('body') : ]) # find()를 통해 admin 부터 그 뒤의 문자열을 출력이 가능하다.

else:
    print("<body> 태그가 존재하지 않습니다.")