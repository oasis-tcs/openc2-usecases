
# endpoint_locate_directory.md

This action triggers a scan to locate the directory path location.

```
{
  "id": "0e7577bd-0996-4097-900b-05de4bc2a2ec",
  "action": "locate",
  "target": {
    "directory": {
      "path": "string"
    }
  },
  "actuator": {
    "process_anti_virus_scanner": {
      "asset_id": "device6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T14:46:36.786Z",
    "stop_time": "2018-06-25T14:46:36.786Z",
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
  "id": "0e7577bd-0996-4097-900b-05de4bc2a2ec",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
