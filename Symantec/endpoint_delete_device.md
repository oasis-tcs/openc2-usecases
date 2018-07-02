
# endpoint_delete_device.md

This action specifies a device deletion from the managemed environment.

```

{
  "id": "046e5e9d-0a4f-40dd-804d-0ed7d0149441",
  "action": "delete",
  "target": {
    "device": {}
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
  "id": "string",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "string"
  }
}
```