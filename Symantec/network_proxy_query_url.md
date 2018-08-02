
# network_proxy_query_url.md

This action retrieves all available information on the specified URL on the actuator.

```
{
  "id": "0f6dc7b5-0cfe-40c2-b032-03dc11e6a308",
  "action": "query",
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
  "id": "0f6dc7b5-0cfe-40c2-b032-03dc11e6a308",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
