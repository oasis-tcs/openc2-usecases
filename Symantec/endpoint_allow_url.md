
# endpoint_allow_url.md

This action specifies that specified URL is allowed to be accessed.

```

{
  "id": "07fd56ac-0c44-402f-8072-0e994de48520",
  "action": "allow",
  "target": {
    "url": {
      "name": "http://www.example.com"
    }
  },
  "actuator": {
    "endpoint": {
      "asset_id": "endpoint6.example.com"
    }
  }
}
```

**RESPONSE**

```
{
  "id": "07fd56ac-0c44-402f-8072-0e994de48520",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
