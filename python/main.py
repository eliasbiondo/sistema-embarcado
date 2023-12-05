import time
from machine import Pin, ADC
import network
import simple as mqtt

import machine
from machine import I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
 
# Inicia o display
LCD_ADDR = 0x27
LCD_NUM_ROWS = 2
LCD_NUM_COLS = 16
LCD_SDA = 16
LCD_SCL = 17
 
i2c = I2C(0, sda=machine.Pin(LCD_SDA), scl=machine.Pin(LCD_SCL), freq=400000)
lcd = I2cLcd(i2c, LCD_ADDR, LCD_NUM_ROWS, LCD_NUM_COLS)

def connect_to_wifi(ssid, password):
    """
    Connect to the specified Wi-Fi network.

    :param ssid: String, the SSID of the Wi-Fi network.
    :param password: String, the password of the Wi-Fi network.
    :return: None
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_attempts = 10
    attempt_count = 0

    while not wlan.isconnected() and attempt_count < max_attempts:
        attempt_count += 1
        print("Connecting to Wi-Fi...")
        time.sleep(1)

    if wlan.isconnected():
        print("Connected to Wi-Fi successfully!")
        print(wlan.ifconfig())
    else:
        print("Failed to connect to Wi-Fi.")

def setup_mqtt_client(client_id, broker, port):
    """
    Setup the MQTT client.

    :param client_id: String, a unique identifier for the MQTT client.
    :param broker: String, the address of the MQTT broker.
    :param port: Int, the network port of the MQTT server.
    :return: An instance of the MQTTClient.
    """
    client = mqtt.MQTTClient(client_id, broker, port)
    client.connect()
    return client

def setup_led_pins():
    """
    Setup the LED pins.

    :return: A tuple of Pin instances for the LEDs.
    """
    led1 = Pin(13, Pin.OUT)
    led2 = Pin(12, Pin.OUT)
    led3 = Pin(11, Pin.OUT)
    return led1, led2, led3

def setup_adc():
    """
    Setup the ADC.

    :return: An ADC instance.
    """
    return ADC(Pin(27))

def main():
    """
    Main program loop.
    """
    # Wi-Fi configuration
    SSID = 'Inteli-COLLEGE'
    PASSWORD = 'QazWsx@123'
    connect_to_wifi(SSID, PASSWORD)

    # MQTT configuration
    MQTT_BROKER = 'test.mosquitto.org'
    MQTT_PORT = 1883
    MQTT_TOPIC = 'sensor/ldr/a8eee424575c6c51bc07d9bd7d8f1277'
    client = setup_mqtt_client('client_id', MQTT_BROKER, MQTT_PORT)

    # Setup LEDs and ADC
    led1, led2, led3 = setup_led_pins()
    adc = setup_adc()

    # Main loop
    while True:
        # Read LDR value
        ldr_value = adc.read_u16()
        print(ldr_value)
        lcd.clear()
        lcd.putstr('Luminosidade: \n' + str(ldr_value))

        # Control LEDs based on LDR value
        if ldr_value < 6000:
            led1.low()
            led2.low()
            led3.low()
        elif 6000 <= ldr_value < 25000:
            led1.high()
            led2.low()
            led3.low()
        elif 25000 <= ldr_value < 55000:
            led1.high()
            led2.high()
            led3.low()
        else:  # ldr_value >= 55000
            led1.high()
            led2.high()
            led3.high()

        # Publish LDR value to MQTT topic
        try:
            client.publish(MQTT_TOPIC, str(ldr_value))
        except Exception as e:
            print('Failed to publish message:', e)

        # Sleep for 1 second
        time.sleep(1)

if __name__ == "__main__":
    main()
