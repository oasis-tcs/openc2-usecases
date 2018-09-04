
# endpoint_restart_device.md

This action restarts a device based on its asset_id.

```

{
  "id": "063f2281-002e-40a3-b038-0d14d80ab9ef",
  "action": "restart",
  "target": {
    "device": {}
  },
  "actuator": {
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T13:52:12.691Z",
    "stop_time": "2018-06-25T13:52:12.691Z",
    "duration": 0,
    "response_requested": "ack",
    "allow_delay": true,
    "occurance": "now",
    "restart_time": "string",
    "randomize": true,
    "prompt": true,
    "prompt_message": "string"
  }
}
```

**RESPONSE**

```
{
  "id_ref": "063f2281-002e-40a3-b038-0d14d80ab9ef",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
