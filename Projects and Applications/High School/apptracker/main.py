from win32gui import GetForegroundWindow
import psutil
import time
import win32process
import datetime
import json
import threading


def update_data(data):
    f = json.load(open("data.json"))
    today = datetime.date.today().strftime("%d-%m-%Y")
    if today not in f:
        f[today] = data
    else:
        f[today] = {i: f[today].get(i, 0) + data.get(i, 0) for i in set(f[today]).union(data)}
    with open("data.json", "w") as file:
        json.dump(f, file)


def check_processes():
    while True:
        process = {}
        timestamp = {}
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        timestamp[current_app] = int(time.time())
        process[current_app] = 1
        update_data(process)
        time.sleep(1)


thread = threading.Thread(target=check_processes)
thread.start()
