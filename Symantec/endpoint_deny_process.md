
# endpoint_deny_process.md

This action specifies a process be denied on an endpoint. e.g Prevent process from executing.

```
{
  "id": "0b1fa41e-07d4-4040-9094-028bba12b206",
  "action": "deny",
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
