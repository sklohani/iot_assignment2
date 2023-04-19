# import Adafruit_DHT
from time import sleep
import requests

address = "http://127.0.0.1:8080/api/dht11"

def read_DHT():
    while True:
        # humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        humidity = 46
        temperature = 29

        print("Humidity: " + str(humidity) + " | Temperature: " + str(temperature))

        payload = {
            'humidity': humidity,
            'temperature': temperature
        }

        print("Sending Payload!")
        try:
            res = requests.post(address, data=payload)

            print(res.json())
        except (KeyboardInterrupt):
            break
        except:
            print("ERR! Can't publish data.")
            
        sleep(20)

if __name__ == "__main__":
    read_DHT()