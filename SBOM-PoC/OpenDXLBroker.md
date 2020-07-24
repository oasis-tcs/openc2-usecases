# OpenDXL Broker 

An OpenDXL Broker is available for all PlugFest participants to connect with and experiment on. There are great open source client libraries available to hit the ground running in [Python](https://github.com/opendxl/opendxl-client-python) and [Java](https://github.com/opendxl/opendxl-client-java). DXL is a cousin of MQTT that is secure by default, [among other differences](https://github.com/opendxl/opendxl-broker/wiki/Comparison-with-MQTT), so please read on to learn how to connect.

# Connecting To The Broker

## Step 1 : Authentication

The OpenDXL Broker requires mutual authentication. In short, you must connect to the broker with a PKI certificate signed by the broker's self-generated Certificate Authority. Luckily, this is a straighforward process. There are a few methods to get a signed key/cert package, shown in order of ease:

_Remember to look in Slack/Discord for a pinned message with the connection details, not shown here._

### Option A: Web Console
Login to the broker's web console and create a signed key package to download:
1. In a browser, go to https://<BROKER_IP>:8443 and click through your browser's security warnings.
2. Login with USERNAME/PW.
3. On the left, click on the "Certificate Management" Icon.
4. Enter:
   * Configureation Type: ```Client Configuration```
   * Common Name: ```Your name or company name```
5. Click "Generate". Done!

### Option B: Ask
* Reach out on Slack/Discord for a complete key package that's already signed.

### Option C: Command Line Utility
If you download the [OpenDXL Python Client](https://github.com/opendxl/opendxl-client-python), it comes with a simple command line utility for this task. You can get a signed key package (as in Option A), or submit your own Certificate Signing Request if you're [using your own private key and cert](#create-your-own-private-key-and-csr).
* This will retrieve a complete signed key package:

    ```dxlclient provisionconfig ./ BROKER_IP YOUR_NAME_OR_COMPANY_NAME```
    
* This will use your own Certificate Signing Request supplied as **client.csr**
   
   ```dxlclient provisionconfig -r ./ BROKER_IP client.csr```
   
In both cases, you'll be prompted for the USERNAME and PW.


### Client.zip
However you proceed, you'll receive **client.zip** that contains:

| File | Description |
| ------ | ----------- |
| ca-bundle.crt   | The broker's certificate. |
| client.crt      | Your signed client certificate. |
| client.key | Your private client key, if you didn't generate your own CSR. |
| dxlclient.config | The broker's IP and port. If using the OpenDXL client libraries mentioned above, this config is generated for them specifically. |


## Step 2 : Connect

* IP Address : Look in your dxlclient.config
* Port : Look in your dxlclient.config

If you are using the OpenDXL client libraries mentioned above, they accept the dxlclient.config file you received above. The quickest Python Hello World program is [here](https://github.com/opendxl/opendxl-client-python/blob/master/examples/basic/event_example.py), but you can just follow these steps:

1. Create a new folder and activate a python virtual env
    * ```mkdir dxl_hello_world && cd dxl_hello_world```
    * ```python -m venv venv && source venv/bin/activate```
1. Download the [latest Python OpenDXL Client](https://github.com/opendxl/opendxl-client-python/releases/download/5.6.0.3/dxlclient-python-sdk-5.6.0.3.zip), then extract the zip file.
    * ```wget https://github.com/opendxl/opendxl-client-python/releases/download/5.6.0.3/dxlclient-python-sdk-5.6.0.3.zip```
    * ```unzip dxlclient-python-sdk-5.6.0.3.zip```
1. Install with pip:
    * ```cd dxlclient-python-sdk-5.6.0.3/lib/```
    * ```pip install dxlclient-5.6.0.3.zip```
1. Insert your config and keys:
    * ```cd ../sample/```
    * Replace **dxlclient.config** with the one you received
    * Place the key files there.
        * **ca-bundle.crt**
        * **client.crt**
        * **client.key**
    * Open **dxlclient.config** and ensure the key file names match.
1. Run the program:
    * ```python basic/event_example.py```
    * You should see a count of about 1000 messages sent/received. If not, something isn't right.
1. A better example to run is in the advanced directory, but requires two shells. It's a clearer demonstration of Pub/Sub, however, and is quick to run.
1. Deactivate the Python environment:
    * ```deactivate```


## Sandboxing

Please sandbox all of your tests by prefixing your name or company to all topic-names and topic-filters. This is not for privacy, but to avoid unknowingly spamming anyone who subscribed to a topic you publish to.

For example, please use this format (with your name, company, etc):

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

## Create your own private key and CSR

Use one of the following commands to create your key and Certificate Signing Request. Be sure and use your name.

* No passphrase:
```bash
    openssl req -out client.csr -subj "/CN=YOUR_NAME_HERE" -new -newkey rsa:2048 -nodes -keyout client.key
```
* Encrypt the private key with a passphrase:
```bash
    openssl req -out MY_CSR -subj "/CN=YOUR_NAME_HERE" -new -newkey rsa:2048 -keyout client.key
```

# Questions

Please reach out on the OpenC2 Discord and Slack channels, we want this to be as easy as possible.
