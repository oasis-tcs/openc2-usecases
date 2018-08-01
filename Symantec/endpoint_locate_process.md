
# endpoint_locate_process.md

This action triggers a scan to locate the process.

```
{
  "id": "0fd151bd-07d3-40bc-80a6-023401a4fa20",
  "action": "locate",
  "target": {
    "process": {
      "name": "otaku.exe",
      "pid": "0"
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
  "id": "0fd151bd-07d3-40bc-80a6-023401a4fa20",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
