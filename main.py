basic.show_number(2)
minutos = 2
alarma = 1

def on_forever():
    global alarma
    if ESP8266_IoT.wifi_state(False):
        basic.show_icon(IconNames.NO)
        ESP8266_IoT.init_wifi(SerialPin.P8, SerialPin.P12, BaudRate.BAUD_RATE115200)
        ESP8266_IoT.connect_wifi("wiot", "a1b2c3d4")
    basic.show_icon(IconNames.YES)
    if Environment.PIR(DigitalPin.P2):
        alarma = 1
    else:
        alarma = 0
    basic.pause(1.5 * 60000)
basic.forever(on_forever)

def on_every_interval():
    if ESP8266_IoT.wifi_state(True):
        basic.show_icon(IconNames.SMALL_DIAMOND)
        ESP8266_IoT.connect_thing_speak()
        basic.show_icon(IconNames.HEART)
        ESP8266_IoT.set_data("JBQ3F7SI645YFNT7",
            randint(30, 50),
            randint(15, 25),
            randint(35, 45),
            randint(0, 2))
        ESP8266_IoT.upload_data()
        basic.show_icon(IconNames.SMALL_HEART)
loops.every_interval(minutos * 60000, on_every_interval)
