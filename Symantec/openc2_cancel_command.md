
# openc2_cancel_command.md

This action cancels a previously sent openc2 command.

```
{
	"id": "0a4a7789-011e-40c8-8004-019214987bab",
	"action": "cancel",
	"target": {
		"command": "07488298-0ce1-408f-80ab-0013e8973266"
	}
}
```

**RESPONSE**

```
{
  "id_ref": "0a4a7789-011e-40c8-8004-019214987bab",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
