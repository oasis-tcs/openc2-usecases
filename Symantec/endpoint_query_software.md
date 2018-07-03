
# endpoint_query_software.md

This action retrieves all available information on the specified software on the actuator.

```
{
  "id": "0145f60f-0a1c-406d-b0a0-06b5ae01fdd7",
  "action": "query",
  "target": {
    "software": {
      "vendor": "vendor_string",
      "name": "otaku.exe",
      "language": "en-us",
      "version": "1.0"
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
  "id": "string",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "string"
  }
}
```