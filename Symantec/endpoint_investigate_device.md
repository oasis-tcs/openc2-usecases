
# endpoint_investigate_device.md

This action gets descriptive data about processes or load point information that have run or have been accessed recently.

```

{
  "id" : "0b6621e7-0b89-4072-b061-0979a27f40bb",
  "action": "investigate",
  "target": {
    "device": {}
  },
  "actuator": {
    "process_anti_virus_scanner": {
      "asset_id": "endpoint6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T13:55:35.341Z",
    "stop_time": "2018-06-25T13:55:35.341Z",
    "duration": 0,
    "response_requested": "ack",
    "include_running": true,
    "include_historical": true,
    "include_prefetch": true,
    "include_loadpoints": true
  }
}
```

**RESPONSE**

```
{
  "id": "0b6621e7-0b89-4072-b061-0979a27f40bb",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
