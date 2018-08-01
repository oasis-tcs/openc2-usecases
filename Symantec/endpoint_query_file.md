
# endpoint_query_file.md

This action queries for the existance of a particular file.

```

{
  "id": "0bd579b8-0c7a-40ad-b0a0-07637abe21b8",
  "action": "query",
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
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  },
  "args": {
    "start_time": "2018-06-25T14:01:03.952Z",
    "stop_time": "2018-06-25T14:01:03.952Z",
    "duration": 0,
    "response_requested": "ack",
    "remediation": {
      "override_process_termination": true,
      "scan_guid": "string"
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
  "id": "0bd579b8-0c7a-40ad-b0a0-07637abe21b8",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
