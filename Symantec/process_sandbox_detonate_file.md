
# process_sandbox_detonate_file.md

This action submits a suspicious file for analysis.

```

{
  "id": "0e2d48bc-07c2-4020-9059-05d88cf31745",
  "action": "detonate",
  "target": {
    "file": {
      "extensions": "string",
      "hashes": {
        "type": "SHA256",
        "value": "string"
      },
      "size": 0,
      "name": "string",
      "name_enc": "string",
      "created": "string",
      "modified": "string",
      "accessed": "string",
      "is_encrypted": true,
      "encryption_algorithm": "string",
      "decryption_key": "string"
    }
  },
  "actuator": {
    "process_sandbox": {
      "asset_id": "detonator6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T13:57:19.030Z",
    "stop_time": "2018-06-25T13:57:19.030Z",
    "duration": 0,
    "response_requested": "ack"
  }
}
```

**RESPONSE**

```
{
  "id": "0e2d48bc-07c2-4020-9059-05d88cf31745",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
