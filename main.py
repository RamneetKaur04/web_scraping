import requests


def fetchAndSaveToFile(url,path):
    r= requests.get(url)
    with open(path,"w") as f:
        f.write(r.text)


url = "https://shop.havenshop.com/collections/cav-empt"

fetchAndSaveToFile(url,"data/havenshop.html")


