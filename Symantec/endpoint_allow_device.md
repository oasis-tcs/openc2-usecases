
# endpoint_allow_device.md

This action specifies that the endpoint actuator allow the device back online. e.g Remove from containment mode.

```
{
  "id": "017b53ed-0a59-4026-b071-092083315645",
  "action": "allow",
  "target": {
    "device": {}
  },
  "actuator": {
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  },
  "options": {
    "start_time": "2018-08-01T17:29:13.150Z",
    "stop_time": "2018-08-01T20:29:13.150Z",
    "duration": 0,
    "response_requested": "ack"
  }
}
```

**RESPONSE**

```
{
  "id": "017b53ed-0a59-4026-b071-092083315645",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
