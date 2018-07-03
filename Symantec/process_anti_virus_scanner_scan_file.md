
# process_anti_virus_scanner_scan_file.md

This action scans for a particular file using the anti-virus scanner component.

```
{
  "id": "0e6c1179-0f35-4076-b0af-003e2f224681",
  "action": "scan",
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
    "process_anti_virus_scanner": {
      "asset_id": "string"
    }
  },
  "args": {
    "start_time": "2018-06-25T13:46:14.013Z",
    "stop_time": "2018-06-25T13:46:14.013Z",
    "duration": 0,
    "response_requested": "ack",
    "type": "QUICK"
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