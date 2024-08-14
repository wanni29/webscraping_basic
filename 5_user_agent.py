# 웹사이트에서는 사용자의 정보를 알수있다. 
# 그것을 `user_agent`  라고 한다.
# 이 정보를 통해서 사람이 접속하는지, 봇이 접속하는지 웹사이트는 판별하며
# 디바이스의 크기를 구해 어떤 화면을 보여줄지 결정하거나 
# 다양한 기능을 수행한다.

# 만약에 웹사이트에 스크랩핑을 하기위해서 코드를 이용해서 접근했는데
# res.raise_for_status()를 통과하지 못하고 권한 문제가 발생한다면
# user_agent를 통해서 권한 문제를 해결해주면 된다.

import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)