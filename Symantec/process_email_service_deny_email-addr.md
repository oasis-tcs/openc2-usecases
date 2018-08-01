
# process_email_service_deny_email-addr.md

This action specifies an email address be denied.

```
{
  "id": "0ebc6bc6-0cd3-40f1-80f9-0b3a4857d21b",
  "action": "deny",
  "target": {
    "email-addr": {
      "value": "number6@village.example.com"
    }
  },
  "actuator": {
    "process_email_service": {
      "asset_id": "mailserver6.example.com"
    }
  }
}
```

**RESPONSE**

```
{
  "id": "0ebc6bc6-0cd3-40f1-80f9-0b3a4857d21b",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
