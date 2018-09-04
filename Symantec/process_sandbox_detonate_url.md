
# process_sandbox_detonate_url.md

This action submits a url for sandbox detonation.

```

{
  "id": "0eb8e4a0-0fc4-4013-a0d2-05402e43fd9d",
  "action": "detonate",
  "target": {
    "url": {
      "name": "http://two.village.example.com"
    }
  },
  "actuator": {
    "process_sandbox": {
      "asset_id": "sandbox6.example.com"
    }
  }
}
```

**RESPONSE**

```
{
  "id_ref": "0eb8e4a0-0fc4-4013-a0d2-05402e43fd9d",
  "status": 200,
  "status_text": "string",
  "results": {
    "command_ref": "INTERNALREFERENCEVALUEABC123"
  }
}
```
