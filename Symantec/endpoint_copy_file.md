
# endpoint_copy_file.md

This action initiates the collection of a file of interest.

```

{
  "id": "04794d16-0dbc-40fd-a099-0151d0a8f025",
  "action": "copy",
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
    "start_time": "2018-06-25T13:59:18.332Z",
    "stop_time": "2018-06-25T13:59:18.332Z",
    "duration": 0,
    "response_requested": "ack",
    "search_location": "filesystem",
    "user_name": "string",
    "user_domain": "string",
    "password": "string"
  }
}
```

**RESPONSE**

```
{
  "id": "04794d16-0dbc-40fd-a099-0151d0a8f025",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
