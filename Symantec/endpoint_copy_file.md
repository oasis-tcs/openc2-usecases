
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
      "asset_id": "string"
    }
  },
  "options": {
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
