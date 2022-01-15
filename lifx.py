# required modules
import requests
import config
import time

if config.lifxEnable:

    # access token
    token = config.lifxKey

    # request header (lifx)
    headers = {
        "Authorization": "Bearer %s" % token,
    }

    # lights

    def default():

        # lifx
        payload = {
            "power": "on",
            "color": "#6e4f23",
            "brightness": "0.3",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def yellow():

        # lifx
        payload = {
            "power": "on",
            "color": "#a3b80b",
            "brightness": "0.5",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def whiteBright():

        # lifx white
        payload = {
            "power": "on",
            "color": "ffffff",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def whiteDim():

        # lifx white
        payload = {
            "power": "on",
            "color": "ffffff",
            "brightness": "0.3",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def orange():

        # lifx
        payload = {
            "power": "on",
            "color": "ff9900",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def orange_slow():

        # lifx
        payload = {
            "power": "on",
            "color": "ff9900",
            "brightness": "1",
            "fast": "false",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def orange_dark():

        # lifx
        payload = {
            "power": "on",
            "color": "de3e04",
            "brightness": "0.4",
            "fast": "false",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def red():

        payload = {
            "power": "on",
            "color": "ed1400",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)


    def flashGreen(duration):

        # lifx green
        payload = {
            "power": "on",
            "color": "00ff00",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
       
        # default
        time.sleep(duration)
        default()

    def flashRed(duration):

        # lifx red on
        payload = {
            "power": "on",
            "color": "ff0000",
            "brightness": "1",
            "fast": "true",
        }
        
        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # default
        time.sleep(duration)
        default()


    def flashYellow(duration):

        # lifx yellow
        payload = {
            "power": "on",
            "color": "faff00",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        # default
        time.sleep(duration)
        default()

    def blue():

        # lifx blue
        payload = {
            "power": "on",
            "color": "0000ff",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def blue_muted():
        # lifx blue
        payload = {
            "power": "on",
            "color": "1893c4",
            "brightness": "0.8",
            "fast": "false",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def pulse_blue():

        # lifx blue
        payload = {
            "power": "on",
            "color": "0000ff",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        time.sleep(0.75)
        default()

    def pulse_green():

        payload = {
            "power": "on",
            "color": "098f04",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        time.sleep(0.75)
        default()

    def pulse_red():

        payload = {
            "power": "on",
            "color": "ff0000",
            "brightness": "1",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

        time.sleep(0.75)
        default()
        
    def dark():
        payload = {
            "power": "on",
            "color": "416675",
            "brightness": "0.3",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def docked_blue():
        payload = {
            "power": "on",
            "color": "0d48bd",
            "brightness": "0.3",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def green():
        payload = {
            "power": "on",
            "color": "0e6305",
            "brightness": "0.5",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)

    def off():
        payload = {
            "power": "off",
            "color": "0e6305",
            "brightness": "0.5",
            "fast": "true",
        }

        response = requests.put('https://api.lifx.com/v1/lights/all/state', data=payload, headers=headers)
        
else:
    print("LIFX Disabled")
