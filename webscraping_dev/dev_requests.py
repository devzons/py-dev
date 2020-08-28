import requests
# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
res.raise_for_status()
# print("Status: ", res.status_code)

# if res.status_code == requests.codes.ok:
#     print("OK")
# else:
#     print("Error. [ErrorCode ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
