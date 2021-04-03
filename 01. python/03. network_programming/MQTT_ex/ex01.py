from mqtt_sub import subscribe

def on_message(client, userdata, msg):
    print(f"{msg.topic} {msg.payload}")

subscribe('localhost', 'iot/#', on_message)