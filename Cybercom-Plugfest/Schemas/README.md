# Schemas
Schemas for three types of OpenC2 actuator devices,
as described in https://github.com/oasis-open/openc2-custom-aps/tree/master/Test:

**Language**,  
**SLPF**, and  
**Language + SLPF + Acme**.

The **Combined** folder has a single schema for each actuator type that validates both commands and responses.
In order to validate a command or response, enclose it in an object with a single **openc2_command** or
**openc2_response** property, e.g.,

```
{
  "openc2_command": {
    "action": "deny",
    "target": {
      "uri": "www.example.com"
    }
  }
}
```

The **Separate** folder has separate schemas for each actuator type that validate just a command or a response, e.g.,

```
{
  "action": "deny",
  "target": {
    "uri": "www.example.com"
  }
}
```

The schemas are in four formats:
1. JADN - source used to generate other formats
2. Markdown - property tables used in published specifications
3. IDL - a text-only alternative to property tables for published specifications
4. JSON Schema - used to validate that JSON data conforms to a specification
