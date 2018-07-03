
# endpoint_stop_process.md

This action stops a specific process.

```

{
  "id": "0ce36ce9-033d-4069-901a-04487e4c6e2e",
  "action": "stop",
  "target": {
    "process": {
      "extensions": "string",
      "is_hidden": true,
      "pid": 0,
      "name": "string",
      "created": "string",
      "cwd": "string",
      "environment_variables": "string"
    }
  },
  "actuator": {
    "endpoint": {
      "asset_id": "string"
    }
  },
  "args": {
    "start_time": "2018-06-25T13:49:53.030Z",
    "stop_time": "2018-06-25T13:49:53.030Z",
    "duration": 0,
    "response_requested": "ack",
    "remediation": {
      "override_process_termination": true
    },
    "allow_quick_search": true,
    "scan_network_paths": true,
    "limit_result_count": 0
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