from datetime import datetime


class Wait:
    load_page = 1.5
    finish_clicks = 0.1
    mouse_move = 0.5


def local_now():
    return datetime.now().strftime("%H:%M:%S")


def click_time(date=6, hour=22, minute=0, second=0):
    return datetime(2021, 1, date, hour, minute, second)


def timestamp():
    milliseconds = 22
    n = datetime.now()
    return " %s | " % str(n)[:milliseconds]
