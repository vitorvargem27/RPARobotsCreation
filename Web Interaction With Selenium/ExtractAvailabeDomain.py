from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as loadTime

navigate = web.Chrome()
navigate.get('https://registro.br/')

userDomain = str(input("Write a domain name for you using :\n")).strip().lower()
domainInputLabel = navigate.find_element(By.ID, 'is-avail-field')
domainInputLabel.send_keys(f"{userDomain}.com.br")
loadTime.sleep(1)
domainInputLabel.send_keys(Keys.ENTER)
loadTime.sleep(2)

result = navigate.find_element(By.XPATH,"/html/body/div/div/main/div/section/div[2]/div/p/span/strong").text
print(result)
if result.lower() == "disponível" :
    print(f'The domain name {userDomain} is available!!')

elif result.lower() == 'não disponível' :
    listDomains = navigate.find_element(By.XPATH, '/html/body/div/div/main/div/section/div[2]/div/div[2]/ul')
    availables = listDomains.find_elements(By.TAG_NAME, 'p')

    for name in availables :
        print(f'The domain \033[1:32m{name.text}\033[m is available!')

loadTime.sleep(10)