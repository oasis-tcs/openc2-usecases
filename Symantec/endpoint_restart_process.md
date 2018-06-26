
# endpoint_restart_process.md

This action specifies a process to start.

```
{
  "id": "05543c9a-0769-408e-8012-048f65cf275d",
  "action": "restart",
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