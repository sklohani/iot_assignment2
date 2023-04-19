import paho.mqtt.subscribe as subscribe
from time import sleep
import json
import ssl

channelID = '<CHANNEL_ID>'
mqttHost = 'mqtt3.thingspeak.com'
topic = 'channels/' + channelID + '/subscribe'
clientID = '<CLIENT_ID>'
auth = {'username': "<USERNAME>",
        'password': "<PASSWORD>"}

useUnsecuredTCP = False
useUnsecuredWebsockets = True
useSSLWebsockets = False

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
    
def mqtt_subscribe():
    print("Subscribing to Topic: " + topic)
    message = subscribe.simple(topics=topic, 
                               hostname=mqttHost, 
                               client_id=clientID, 
                               transport=tTransport, 
                               port=tPort, 
                               tls=tTLS, 
                               auth=auth)

    data = json.loads(message.payload.decode('ascii'))
    # print(data)

    timeStamp = data['created_at']
    dateTime = timeStamp.split('T')
    date = dateTime[0]
    time = dateTime[1][:-1]

    return_str = f"Date: {date}, Time: {time} :: Temperature: {data['field1']} | Humidity: {data['field2']}"
    print(return_str)
    return return_str

# mqtt_subscribe()