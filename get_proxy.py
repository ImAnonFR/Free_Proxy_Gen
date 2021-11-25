import requests
from time import sleep
import json


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0',
    }
    content = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all", headers=headers)
    sleep(3)
    result = content.text
    result = result.replace("\n", "")
    text_file = open("http.txt", "w")
    text_file.write(result)
    text_file.close()
    

