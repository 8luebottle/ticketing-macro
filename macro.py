import pyautogui
import webbrowser

from time import sleep
from icecream import ic

ic("open browser")
url = "url here"
webbrowser.get("chrome").open(url)

ic("scroll")
pyautogui.click(800, 730)
sleep(0.5)
pyautogui.moveTo(800, 600)
for i in range(13):
    pyautogui.scroll(-10)

