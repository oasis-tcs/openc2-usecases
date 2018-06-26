
# endpoint_cancel_command.md

This action cancels a previously sent openc2 command.

```
{
  "id": "0a4a7789-011e-40c8-8004-019214987bab",
  "action": "cancel",
  "target": {
    "openc2": {
      "command": "07488298-0ce1-408f-80ab-0013e8973266"
    }
  },
  "actuator": {
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  }
}
```