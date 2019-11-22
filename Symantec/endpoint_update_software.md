
# endpoint_update_software.md

This action updates the specified software.

```
{
  "id": "0634fd62-054d-4043-a0a6-08f0a34c6c3b",
  "action": "update",
  "target": {
    "software": {
      "name": "otaku.exe",
      "language": "en-us",
      "vendor": "vendorString",
      "version": "14"
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
  "id_ref": "0634fd62-054d-4043-a0a6-08f0a34c6c3b",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
