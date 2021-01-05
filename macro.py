import pause
import pyautogui
import webbrowser

from time import sleep
from icecream import ic

import ticketing.mouse_positions as position
from confs.config import conf
from ticketing.errors import formatted_error
from ticketing.times import timestamp, click_time, Wait


ic.configureOutput(prefix=timestamp)
Site = conf["site"]


ic("🤖 : Start my job")
ic("open the browser")
webbrowser.get("chrome").open_new_tab(Site.url())


ic("Click the browser")
pyautogui.click(position.APPLY_BTN)
sleep(Wait.load_page)


ic("Scroll down")
for i in range(13):
    pyautogui.scroll(-10)


ic("Pause for click time")
pause.until(click_time(hour=2, minute=18, second=10))


total_clicks = 0
ic("Click {} time(s)".format(total_clicks))
pyautogui.click(clicks=total_clicks)
sleep(Wait.finish_clicks)


ic("move mouse cursor to the next button")
pyautogui.moveTo(position.CONFIRM_BTN)
sleep(Wait.mouse_move)


ic("click the confirm button")
pyautogui.click(clicks=total_clicks)


ic("Wait for click")
sleep(1)

ic("🤖 : I'm done.")
