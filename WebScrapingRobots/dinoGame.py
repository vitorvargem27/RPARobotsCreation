import pyautogui
import pyautogui as action
import pyautogui as keyboard
import pyautogui as loadTime
import random

keyboard.hotkey('win', 'r')
action.typewrite('https://chromedino.com/')
keyboard.press('enter')
loadTime.sleep(5)
keyboard.press('space')
loadTime.sleep(3)

while True :
    try :
        img01 = action.locateOnScreen('cactoJogo.PNG', 1.5, confidence=0.7)
        img02 = action.locateOnScreen('cacto2Jogo.PNG', 1.5, confidence=0.7)
        img03 = action.locateOnScreen('cacto3Jogo.PNG', 1.5, confidence=0.7)
        img04 = action.locateOnScreen('cacto4Jogo.PNG', 1.5, confidence=0.7)
        img05 = action.locateOnScreen('cacto5Jogo.PNG', 1.5, confidence=0.7)
        img06 = action.locateOnScreen('cacto5Jogo.PNG', 1.5, confidence=0.7)

        if img01 is not None :
            keyboard.press('space')
            print('Pulando01')

        elif img02 is not None :
            keyboard.press('space')
            print('Pulando02')

        elif img03 is not None :
            keyboard.press('space')
            print('Pulando03  ')

        elif img04 is not None :
            keyboard.press('space')
            print('Pulando03  ')

        elif img05 is not None :
            keyboard.press('space')
            print('Pulando03  ')

        elif img06 is not None :
            keyboard.press('space')
            print('Pulando03  ')

    except pyautogui.ImageNotFoundException :
        print('Cacto não localizado')