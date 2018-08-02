
# endpoint_start_process.md

This action specifies a process to start.

```
{
  "id": "04be1c1b-0d81-400b-9085-015a7746e401",
  "action": "start",
  "target": {
    "process": {
      "name": "otaku.exe"
    }
  },
  "actuator": {
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  }
}
```

**RESPONSE**

```
{
  "id": "04be1c1b-0d81-400b-9085-015a7746e401",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
