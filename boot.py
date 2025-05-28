import network
import time
import config

SSID = config.SSID
PASSWORD = config.PASSWORD

def connect_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        wlan.connect(ssid, password)
        timeout = 10
        while not wlan.isconnected() and timeout > 0:
            time.sleep(1)
            timeout -= 1
    if wlan.isconnected():
        print('Connected:', wlan.ifconfig()[0])
    else:
        print('Failed to connect Wi-Fi')

connect_wifi(SSID, PASSWORD)
