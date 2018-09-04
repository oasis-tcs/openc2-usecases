
# process_email_service_deny_email-message.md

This action specifies that an email matching email-message target values be denied.

```
{
  "id": "04b5bf32-0a7f-40bb-8071-05da4da1cda9",
  "action": "deny",
  "target": {
    "email-message": {
      "to": "string@string",
      "from": "string@string",
      "subject": "string",
      "cc": "string@string",
      "bcc": "string@string"
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
  "id_ref": "04b5bf32-0a7f-40bb-8071-05da4da1cda9",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
