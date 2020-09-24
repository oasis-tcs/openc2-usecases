# OpenC2 MQTT Broker

A publicly available MQTT broker is setup to test OpenC2 Messages over MQTT. This is a sandbox for testing OpenC2, so please connect, subscribe, and start publishing!

It's a RabbitMQ server configured for MQTT, and will be up 24/7 except for any maintenance.

No MQTT topics-names or topic-filters are defined on the server itself; they are ephemeral, defined on-the-fly by clients that publish and subscribe. Please see the notes below about sandboxing your tests.

# Connecting To the MQTT Broker

_Remember to look in Slack/Discord for a pinned message with the connection details, not shown here._

## Insecure Access:

With the IP, Port, User, and Password, you can use any MQTT client to connect to the broker over an unencrypted TCP connection. Look at the [Hello World section below](#example-hello-world) for an example.

## TLS Access:

There are two ways to connect with TLS. These options assume you are using the [Hello World example](#example-hello-world) below.

### Option A: Ignore Broker Identity
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
### Option B: Verify Broker Identity
To verify the broker's identity, you'll need its [CA certificate](#broker-ca-certificate), referenced here as **ca-broker.crt**:
```python
import ssl
# ... client already created
CA_CERTS = 'path/to/ca-broker.crt'
context = ssl.create_default_context()
context.load_verify_locations(cafile=CA_CERTS)
client.tls_set_context(context)
# ... now connect client
```
# Use Draft OpenC2 MQTT Transfer Specification

The plugfest will use WD04 of the in-development OpenC2 Transfer Specification as the working standard for use of MQTT.  This version of the document can be found at:

https://github.com/oasis-tcs/openc2-transf-mqtt/blob/v1.0_wd04/transf-mqtt-v1.0.md

This specification incorporates, in [Section 2.3](https://github.com/oasis-tcs/openc2-transf-mqtt/blob/v1.0_wd04/transf-mqtt-v1.0.md#23-message-format), a proposed new OpenC2 message format with more complete contents, originally presented in [issue #353](https://github.com/oasis-tcs/openc2-oc2ls/issues/353) for the OpenC2 Language Specification, along with an initial 2-byte field in the message payload to specify the serialization and message type contained in the remainder of the MQTT PUBLISH control packet payload.

This approach means using MQTT v3.1.1 clients and applying the concepts described in the specification for topics structure, message format, etc.  Any gaps in the spec should be addressed in the context of the plug fest to achieve interoperability, with the understanding that solutions developed there will be considered for later incorporation into the spec as it develops.


# Topic Structure and Namespaces for Separation

The plugfest will use the default topic structure described in [Section
2.2](https://github.com/oasis-tcs/openc2-transf-mqtt/blob/v1.0_wd04/transf-mqtt-v1.0.md#22-default-topic-structure)
of the draft MQTT specification. However, in order to permit groups within the plugfest a limit space for testing, the plugfest will add a top-layer topic to the structure to create informal namespace partitioning of the topic structure. Producers and Consumers connected to the broker who wish to be available to any interested communications peer should prefix their topic subsubscriptions and message publising with `vpf` (virtual plug fest).  Groups of participants who wish to focus their communications should select a namespace related to their group or organization and adjust their subscriptions and publications accordingly. For example a group focused on firewalls might use `fw`, leading to topics like:
```
fw/oc2/cmd/all
fw/oc2/cmd/slpf
```
Topic subscriptions and publications with out a namespace prefix should be avoided.


# Example: Hello World

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

# Using TLS? Insert context code here

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
    
# Using TLS? Create an ssl context here and supply it as the 'tls' argument below.

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
# Broker CA Certificate
To verify the broker's identity over a TLS connection, use the following CA certificate:

```
-----BEGIN CERTIFICATE-----
MIIC8TCCAdmgAwIBAgIUfSYzn1Apcjkvxbhn6WVSRbGHmJkwDQYJKoZIhvcNAQEL
BQAwITEfMB0GA1UEAwwWTVFUVENsaWVudENBLTIwMjAwNzI4QTAeFw0yMDA3Mjgx
NzQyMDFaFw0zMDA3MjYxNzQyMDFaMCExHzAdBgNVBAMMFk1RVFRCcm9rZXJDQS0y
MDIwMDcyOEEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDIwOjaMOiW
tVmnZvPxVBcupxMmOEp5TfFsBGA6bS2DwphGfBHmNZLYnvlYlc4Rav2vXowouPOs
J8F+6uCjdzr11pJn21QyPoa70RVH4gHhxXu6A6DuSn7mtUWWyJB5OPU7pPGAe/bf
4VQcYDQBaPww1jyunXWp5E5ZZKcWw0T8lSZTCHNH0HiLxjk/kGvqw0GkRUd5pMWR
RdyAdC7ShOUJgEq82aREFHl1Q9MXz2/pnf+boSM05tLblmXQMn6mk8ARp7uwA85A
Aorw7WyyimL4NsvKLn7Ctr/pwMgQYq//27lwzb95gmE2ZMVVf2Fk86qZObTUpj/F
acj6otHzUOHjAgMBAAGjITAfMAwGA1UdEwQFMAMBAf8wDwYDVR0RBAgwBocEIlZ1
cTANBgkqhkiG9w0BAQsFAAOCAQEAIuAqE5H3RvgFQRvEuk4buS1gLqXICsEW8Me6
W0b5m6cQUqbRSzgsqjHC9B6BnddO2wiP2RafoSyJ9PKDffBHXAaY58REpw8jqTaY
DtrePn6fWsf+e7Chj5mGkudTQ9xYuWjpblOzeuev0CketEtfXNyakBLpmFAtnVpy
nVnmQsei9LETs2qDhtacy6P2jJ9o+q9PEl0BFBi/9w8eJUVxIOceVSfKQjr7C7xU
/ajbowCj7arCAlk78Om5+QuufKr9XSrPZKAPbEcMnZwyyxIT4s0jctx9+KU4cxUU
Op37Dg4+MftZyaIJzhaWPl/Dh7tVxJpZo/CSFjLIl6Fh1wxabw==
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDIzCCAgugAwIBAgIUGQJnbKgR6zhFnSH9XpdVoiw0dPYwDQYJKoZIhvcNAQEL
BQAwITEfMB0GA1UEAwwWTVFUVENsaWVudENBLTIwMjAwNzI4QTAeFw0yMDA3Mjgx
NzQyMDFaFw0zMDA3MjYxNzQyMDFaMCExHzAdBgNVBAMMFk1RVFRDbGllbnRDQS0y
MDIwMDcyOEEwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDbxSlzp50h
LI6MqunOa9Kl71z8aT96bIW8ZgCz4hLWBQrLagYsCRk9AkkVJBrg9CuLGMGjrawJ
tNNki50DgHAl6gGciDaHmF6OgthDo/1NjaZ/2x1f4SQUBvBjadSnIyvkDPeL+VLB
8CimBrrSI7jMwnSTN3Gelwh4lpg26NJpHGwrx0sW1hi3JOX1sBbg2GOKPJjCL2zt
iDZcEYEg/VU7XdZoGRYJrK6kazrK3qVy+A5pTQ7SaWqUyWaJmSWY8Ypm0WK7yHtY
OCJ9JQwlTaMJiLky9FD4EJMNrEcsudBBY37yupUApK3uTxdMFxxdgGhHbh4aIvEa
0K+LxJ9umn+tAgMBAAGjUzBRMB0GA1UdDgQWBBTVJ4euaHHiO9DGoFQxxqG8W60Q
sDAfBgNVHSMEGDAWgBTVJ4euaHHiO9DGoFQxxqG8W60QsDAPBgNVHRMBAf8EBTAD
AQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBZPJ+VCuigERX9t3kNtlCYwg9eJgAr5LfP
7faK10UgV0/UqN/FxiTrFV34FALg/T+eqmB1N/7KeW0JVZDX6U85LZlynxpY6oy+
pE0l/plDZq/IfKIZFivJI/KQ22g6LN3Vc2WxNzjTLfsjulSyqc/TfiJ4rImXZ4YQ
PFAvNkbpJn9VRIwANUc4oV0DFKCRsWiP3HzQBNnounjJamiTGMpMtkwFQowYDPGX
qeeDbik+b8gTa7Wz8SvmcyLrdma4jQEJ/hZcyJCh7DPHhpvA/KPkpOmjxmKKgpCQ
o6XemQjPDW+inFvq16L1KeLpnJCCfWsTSnYhZCX8DjsAzbrNn3pN
-----END CERTIFICATE-----
```

# Questions

Please reach out on the OpenC2 Discord and Slack channels, we want this to be as easy as possible.
