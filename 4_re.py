import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

# p -> 패턴
# m -> 매칭
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case (o) | caffe (x)
# ^ (^de) : 문자열의 시작 > desk, destination (o) | fade (x)
# $ (se$) : 문자열의 끝 > case, base (o) | face (x)
p = re.compile("ca.e") 

def print_match(m) :
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

# 주어진 문자열의 처음부터 일치하는지 확인 하는것 이기때문에
# care외로 뒤에 어떠한 값이 있어도 처음부터 일치하기에 넘어가는것이다.
m = p.match("careless")
print_match(m)