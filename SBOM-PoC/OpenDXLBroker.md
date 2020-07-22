# OpenDXL Broker 

An OpenDXL Broker is available for all PlugFest participants to connect with and expirement on. There are great open source client libraries available to hit the ground running in [Python](https://github.com/opendxl/opendxl-client-python) and [Java](https://github.com/opendxl/opendxl-client-java). DXL is a cousin of MQTT that is secure by default, [among other differences](https://github.com/opendxl/opendxl-broker/wiki/Comparison-with-MQTT), so please read on to learn how to connect.

# Connecting To The Broker

## Authentication

The OpenDXL Broker requires mutual authentication. In short, you must connect to the broker with a PKI certificate signed by the broker's self-generated Certificate Authority. Luckily, this is a straighforward process. There are two methods:

* [Create your own CSR](#create-your-own-private-key-and-csr) (Certificate Signing Request), then send it to the OpenC2 Team to sign and return to you.

or

* Request a signed key package. This is easier, but exposes your private key.

However you proceed, you'll receive **client.zip** that contains:

| File | Description |
| ------ | ----------- |
| ca-broker.crt   | The broker's certificate. |
| client.crt      | Your signed client certificate. | 
| dxlclient.config | The broker's IP and port. If using the OpenDXL client libraries mentioned above, this config is generated for them specifically. |
| client.key | Your private client key, if you didn't generate your own CSR. |


## Connect

If you are using the OpenDXL client libraries mentioned above, they accept the dxlclient.config file your received above. The quickest Python Hello World program is [here](https://github.com/opendxl/opendxl-client-python/blob/master/examples/basic/event_example.py), but you can just follow these steps:

1. Create a new folder and activate a python virtual env
    * ```mkdir dxl_hello_world && cd dxl_hello_world```
    * ```python -m venv venv && source venv/bin/activate```
1. Download the [latest Python OpenDXL Client](https://github.com/opendxl/opendxl-client-python/releases/download/5.6.0.3/dxlclient-python-sdk-5.6.0.3.zip), then extract the zip file.
1. Navigate to the lib folder
    * ```pip install dxlclient-5.6.0.2.zip```
1. Navigate to the samples directory:
    * Replace the dxlclient.config with the one you received
    * Place the keys you recieved there as well
1. Run the program:
    * ```python basic/event_example.py```
    * You should see a count of about 1000 messages sent/received. If not, something isn't right.
1. A better example to run is in the advanced directory, but requires two shells. It's a clearer demonstration of Pub/Sub, however, and is quick to run.
1. Deactivate the Python environment:
    * ```deactivate```




## Create your own private key and CSR

Use one of the following commands to create your key and Certificate Signing Request. Be sure and use your name.

* Encrypt the private key with a passphrase:
```bash
    openssl req -out client.csr -subj "/CN=YOUR_NAME_HERE" -new -newkey rsa:2048 -nodes -keyout client.key
```
* No passphrase:
```bash
    openssl req -out MY_CSR -subj "/CN=YOUR_NAME_HERE" -new -newkey rsa:2048 -keyout client.key
```

# Questions

Please reach out on the OpenC2 Discord and Slack channels, we want this to be as easy as possible.
