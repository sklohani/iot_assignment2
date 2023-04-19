import paho.mqtt.publish as publish
import Adafruit_DHT
from time import sleep
import ssl

channelID = '<CHANNEL_ID>'
mqttHost = 'mqtt3.thingspeak.com'
topic = 'channels/' + channelID + '/publish'
clientID = '<CLIENT_ID>'
auth = {'username': "<USERNAME>",
        'password': "<PASSWORD>"}

useUnsecuredTCP = False
useUnsecuredWebsockets = False
useSSLWebsockets = True

if useUnsecuredTCP:
    tTransport = 'tcp'
    tPort = 1883
    tTLS = None

if useUnsecuredWebsockets:
    tTransport = 'websockets'
    tPort = 80
    tTLS = None

if useSSLWebsockets:
    tTransport = 'websockets'
    tPort = 443
    tTLS = {'ca_certs': "/etc/ssl/certs/ca-certificates.crt",
            'tls_version': ssl.PROTOCOL_TLSv1}

def read_DHT():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)

        print("Humidity: " + str(humidity) + " | Temperature: " + str(temperature))

        tPayload = 'field1=' + str(humidity) + '&field2=' + str(temperature)

        print("Publishing to Topic: " + topic)
        try:
            publish.single(topic=topic, 
                           payload=tPayload, 
                           hostname=mqttHost, 
                           transport=tTransport, 
                           port=tPort, 
                           tls=tTLS, 
                           client_id=clientID, 
                           auth=auth)
        except (KeyboardInterrupt):
            break
        except:
            print("ERR! Can't publish data.")
            
        sleep(5)

if __name__ == "__main__":
    read_DHT()