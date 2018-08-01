
# endpoint_delete_file.md

This action specifies a file to be deleted.

```
{
  "id": "0969391d-0f18-40a3-8046-05c312e97b5b",
  "action": "delete",
  "target": {
    "file": {
      "extensions": "string",
      "hashes": {
        "type": "SHA256",
        "value": "dc94bbd73a1fce1b04c663a008408dd209cfe355483eea2044f2a4616aad7110"
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
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T19:31:17.916Z",
    "stop_time": "2018-06-25T19:31:17.916Z",
    "duration": 0,
    "response_requested": "ack",
    "remediation": {
      "override_process_termination": true
    },
    "allow_quick_search": true,
    "scan_network_paths": true,
    "limit_result_count": 0
  }
}
```

**RESPONSE**

```
{
  "id": "0969391d-0f18-40a3-8046-05c312e97b5b",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
