
# network_proxy_deny_url.md

This action specifies a url be blocked from access.

```
{
  "id": "0c4f641d-0cbb-4063-b041-0ec7e718051b",
  "action": "deny",
  "target": {
    "url": {
      "name": "http://village.example.com"
    }
  },
  "actuator": {
    "network_proxy": {
      "asset_id": "gateway2.example.com"
    }
  }
}
```

**RESPONSE**

```
{
  "id": "0c4f641d-0cbb-4063-b041-0ec7e718051b",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
