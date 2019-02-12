# Description
This use-case shows a working example of a command/response workflow with status requests and updates. The purpose of this example is to explore the use of `request_id` and `command_id`. This example uses HTTPS as the tranfer protocol, which maps `request_id` to `X-Correlation-ID` found in the header. The `command_id` is found in the body of the payload.

The identifiers used in this example are for illustrative purposes and may not conform to the actual identifier format.

## 1. Initial Command Is Issued
### 1.1. Command
```
POST /openc2 HTTP/1.1
Host: oc2consumer.company.net
Content-type: application/openc2-cmd+json;version=1.0
Date: Day, DD Mon YYYY HH:MM:SS GMT
X-Correlation-ID: 0001

{	
    "command_id": "cmd5",
    "action": "scan",
    "target": {
         "file": {...}
    },
    "args": {
        "response_requested": "ack"
    }
}
```

### 1.2. Response
```
HTTP/1.1 200 OK
Date: Day, DD Mon YYYY HH:MM:SS GMT
Content-type: application/openc2-rsp+json;version=1.0
X-Correlation-ID: 0001

{	
    "status": 102
}
```

## 2. Status Is Requested
### 2.1. Command
```
POST /openc2 HTTP/1.1
Host: oc2consumer.company.net
Content-type: application/openc2-cmd+json;version=1.0
Date: Day, DD Mon YYYY HH:MM:SS GMT
X-Correlation-ID: 0002

{	
    "action": "query",
    "target": {
         "command": "cmd5"
    },
    "args": {
        "response_requested": "status"
    }
}
```

### 2.2. Response
```
HTTP/1.1 200 OK
Date: Day, DD Mon YYYY HH:MM:SS GMT
Content-type: application/openc2-rsp+json;version=1.0
X-Correlation-ID: 0002

{	
    "status": 102,
    "strings": [...]
}
```

## 3. Command Is Canceled
### 3.1. Command
```
POST /openc2 HTTP/1.1
Host: oc2consumer.company.net
Content-type: application/openc2-cmd+json;version=1.0
Date: Day, DD Mon YYYY HH:MM:SS GMT
X-Correlation-ID: 0003

{	
    "action": "cancel",
    "target": {
         "command": "cmd5"
    }
}
```

### 3.2. Response
```
HTTP/1.1 200 OK
Date: Day, DD Mon YYYY HH:MM:SS GMT
Content-type: application/openc2-rsp+json;version=1.0
X-Correlation-ID: 0003

{	
    "status": 200,
    "strings": [...]
}
```
