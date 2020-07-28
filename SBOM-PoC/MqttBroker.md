# OpenC2 MQTT Broker

A publicly available MQTT broker is setup to test OpenC2 Messages over MQTT. This is a sandbox for testing OpenC2, so please connect, subscribe, and start publishing!

It's a RabbitMQ server configured for MQTT, and will be up 24/7 except for any maintenance.

No MQTT topics-names or topic-filters are defined on the server itself; they are ephemeral, defined on-the-fly by clients that publish and subscribe. Please see the notes below about sandboxing your tests.

_Remember to look in Slack/Discord for a pinned message with the connection details, not shown here._

## Insecure Access:

With the IP, Port, User, and Password, you can use any MQTT client to connect to the broker over an unencrypted TCP connection. Look at the [Hello World section below](#example-hello-world) for an example.

## TLS Access:

There are two ways to connect with TLS. These options assume you are using the Hello World example below.
### Option A: Less Secure
If you aren't concerned with the broker's identity, just add a basic ssl context:
```python
import ssl
# ... client already created
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
client.tls_set_context(context)
# ... now connect client
```
### Option B: More Secure
To verify the server's identity, you'll need its CA certificate:
```python
import ssl
# ... client already created
CA_CERTS = 'path/to/ca-broker.crt'
context = ssl.create_default_context()
context.load_verify_locations(cafile=CA_CERTS)
client.tls_set_context(context)
# ... now connect client
```
## Sandboxing

Please sandbox all of your tests by prefixing your name to all topic-names and topic-filters. This is not for privacy, but to avoid unknowingly spamming anyone who subscribed to a topic you publish to.

For example, please use this format (with your name):

```
patrickc/oc2/cmd/
patrickc/#
patrickc/foo/bar
```

Do not use:
```
oc2/cmd/
#
foo/bar
```


## Example: Hello World

To get started, here is a simple Python3 example with a publisher sending a message to a subscriber.

**Bash shell**
```bash
mkdir test_mqtt
cd test_mqtt
python3 -m venv venv
source venv/bin/activate
pip install paho-mqtt
mkdir test1
cd test1
touch mqtt_subscriber.py
touch mqtt_publish.py
touch mqtt_config.py
```

**mqtt_config.py**

If your code might be stored on GitHub or other public location, please ensure that it does not contain
[access credentials](https://geekflare.com/github-credentials-scanner/)
([CWE](https://cwe.mitre.org/data/definitions/798.html)).  Your mqtt_config.py should obtain credentials from a local configuration file, environment variable, etc.
```python
YOUR_NAME_PREFIX = # Your name, Eg "johnd/"
broker_ip = "*.*.*.*"
broker_port = ****
user_name = '****'
user_pw   = '****'
```

**mqtt_subscriber.py**
```python
#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import mqtt_config as config

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(config.YOUR_NAME_PREFIX + "oc2/cmd")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.username_pw_set(config.user_name, password=config.user_pw)
client.on_connect = on_connect
client.on_message = on_message

client.connect(config.broker_ip, config.broker_port, 60)

client.loop_forever()
```

**mqtt_publish.py**
```python
#!/usr/bin/env python3

import paho.mqtt.publish as publish
import mqtt_config as config

login = {'username':config.user_name, 'password':config.user_pw}

query_features = {
        "action": "query",
        "target": {
            "features": []
        },
        "args": {
            "response_requested": "complete"
        }
    }

publish.single(config.YOUR_NAME_PREFIX + "oc2/cmd", payload=str(query_features), qos=0,
    retain=False, hostname=config.broker_ip, port=config.broker_port, client_id="", 
    keepalive=60, will=None, auth=login, tls=None)
```

Now start the subscriber in one shell, then run the publisher in another, eg:

**Original Shell**
```bash
python mqtt_subscriber.py
```

**New Shell**
```bash
source ../venv/bin/activate
python mqtt_publish.py
```

