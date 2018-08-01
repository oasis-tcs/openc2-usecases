
# endpoint_locate_windows_registry_key.md

This action triggers a scan to locate the windows registry key.

```
{
  "id": "0fbfb8fa-0887-40a6-800d-070118482d03",
  "action": "locate",
  "target": {
    "windows_registry_key": {
      "key": "string"
    }
  },
  "actuator": {
    "process_anti_virus_scanner": {
      "asset_id": "device6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T14:47:34.109Z",
    "stop_time": "2018-06-25T14:47:34.109Z",
    "duration": 0,
    "response_requested": "ack",
    "allow_quick_search": true,
    "scan_network_paths": true,
    "limit_result_count": 0
  }
}
```

**RESPONSE**

```
{
  "id": "0fbfb8fa-0887-40a6-800d-070118482d03",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
