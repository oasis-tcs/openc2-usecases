
# process_anti_virus_scanner_restore_file.md

This action restores a file that was previously quarantined or isolated in some manner.

```

{
  "id": "0da8db5b-010f-4056-80a9-0955074dfcb1",
  "action": "restore",
  "target": {
    "file": {
      "extensions": "string",
      "hashes": {
        "type": "SHA256",
        "value": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
      },
      "size": 0,
      "name": "netgato.exe",
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
      "asset_id": "device6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T13:53:37.231Z",
    "stop_time": "2018-06-25T13:53:37.231Z",
    "duration": 0,
    "response_requested": "ack"
  }
}
```

**RESPONSE**

```
{
  "id_ref": "0da8db5b-010f-4056-80a9-0955074dfcb1",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
