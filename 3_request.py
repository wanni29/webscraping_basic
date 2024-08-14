import requests

# 웹스크랩핑을 하기 위해서 코드를 올바르게 가지고 왔다.
# 이 코드 두줄은 웹스크랩핑을 진행하기 위해서 거의 고정코드로 사용하는 코드임
res = requests.get("http://google.com")
res.raise_for_status() 

# if res.status_code == requests.codes.ok: # ok == 200
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 {res.status_code}]".format(res.status_code))

print(len(res.text))
print(res.text)

with open("my_google.html", "w", encoding="utf8") as f:
    f.write(res.text)