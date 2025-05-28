import time
from machine import Pin
import urequests
import ujson

import config  

FRIDGE_PIN = config.FRIDGE_PIN
FREEZER_PIN = config.FREEZER_PIN


door_status = {
    "冷蔵庫": {"pin": Pin(FRIDGE_PIN, Pin.IN, Pin.PULL_UP), "opened_at": None, "notified": False},
    "冷凍庫": {"pin": Pin(FREEZER_PIN, Pin.IN, Pin.PULL_UP), "opened_at": None, "notified": False}
}
THRESHOLD = 60  

def send_line_message(message):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + config.ACCESS_TOKEN
    }
    body = {
        "to": config.USER_ID,
        "messages": [{"type": "text", "text": message}]
    }
    try:
        res = urequests.post(config.LINE_API_URL, headers=headers, data=ujson.dumps(body).encode('utf-8'))
        print(res.text)
        res.close()
    except Exception as e:
        print("Request Error:", e)


time.sleep(2)
alert_emojis = "⚠️" * 12

while True:
    now = time.time()
    for name, info in door_status.items():
        pin = info["pin"]
        if pin.value() == 1: 
            if info["opened_at"] is None:
                info["opened_at"] = now
            elif not info["notified"] and (now - info["opened_at"] > THRESHOLD):
                send_line_message(f"{alert_emojis}\n{name}のドアが1分以上開いています!!\n{alert_emojis}")
                info["notified"] = True
        else:
            info["opened_at"] = None
            info["notified"] = False
    time.sleep(1)
