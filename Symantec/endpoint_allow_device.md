
# endpoint_allow_device.md

This action specifies that the endpoint actuator allow the device back online. e.g Remove from containment mode.

```

{
  "id": "017b53ed-0a59-4026-b071-092083315645",
  "action": "allow",
  "device": {},
  "actuator": {
    "endpoint": {
      "asset_id": "string"
    }
  },
  "args": {
    "start_time": "2018-06-25T14:01:03.952Z",
    "stop_time": "2018-06-25T14:01:03.952Z",
    "duration": 0,
    "response_requested": "ack",
  }
}
```

**RESPONSE**

```
{
  "id": "string",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "string"
  }
}
```
