
# endpoint_locate_file.md

This action triggers a scan to locate the files location.

```
{
  "id": "062bb458-081e-40d3-a0e8-05326290d542",
  "action": "locate",
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
    "start_time": "2018-06-25T13:45:21.908Z",
    "stop_time": "2018-06-25T13:45:21.908Z",
    "duration": 0,
    "response_requested": "ack",
    "allow_quick_search": true,
    "scan_network_paths": true,
    "limit_result_count": 0
  }
}
```