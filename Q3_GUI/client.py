import Adafruit_DHT
from time import sleep
import requests

address = "http://127.0.0.1:8080/api/dht11"

def read_store():
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print("Humidity: " + str(humidity) + " | Temperature: " + str(temperature))

    payload = {
        'humidity': humidity,
        'temperature': temperature
    }

    print("Sending Data!")
    try:
        res = requests.post(address, data=payload)

        print(res.json())
        msg = f"Humidity: {res.json()['humidity']} | Temperature: {res.json()['temperature']}"
    except:
        msg = "ERR! Can't store data."
        print(msg)
    
    return msg

def getDB():
    print("Getting Data!")
    try:
        res = requests.get(address)

        msg = res.json()
        print(msg)
    except:
        msg = "ERR! Can't fetch data."
        print(msg)
    
    return msg