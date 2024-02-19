import requests
from bs4 import BeautifulSoup

page = requests.get("https://discord.com/channels/1176565746638270577/1176565746638270583")

if page.status_code == 200 :
    allCodePage = BeautifulSoup(page.text, "html.parser")
    quantity = 0

    for link in allCodePage.find_all("link") :
        quantity += 1
        print(f"Link {quantity} : {link}")

else :
    print('HTTP error ', page.status_code)

import pdb;pdb.set_trace()

