import requests

def check_rbx_v():
    rbx_api_url = "https://setup.roblox.com/version"
    respponse = requests.get(rbx_api_url)
    
    if respponse.status_code == 200:
        curnt_v = respponse.text
        print("current roblox version: " + curnt_v)
    else:
        print("smthing went wrong")

check_rbx_v()
