# 1 Retrieve a value from an actuator
This example shows the OpenC2 Command and Response for retrieving data from an actuator.

The data to retrieve is a property called "battery_percentage".

The actuator is the Tesla Power Wall.

from the tesla api:  `192.168.110.210/api/system_status/soe`

This same example could work for create, set, and delete, although certain properties may not work for all 4 CRUD actions.

## 1.1 Examples
### 1.1.1 OpenC2 Command
```
{
    "command_id": "01076931758653239640628182951035",
    "action": "query",
    "target": {
        "properties": [
            "battery_percentage"
        ]
    },
    "actuator": {
        "endpoint_smart_meter": {
            "actuator_id": "TSLA-00101111",
            "asset_id": "TGEadsasd"
        }
    }
}
```

### 1.1.2 OpenC2 Response
```
{
    "status": 200,
    "results": {
        "x-acme": {
            "battery_percentage": 0.577216
        }
    }
}
```

## 1.2 Property Tables
### 1.2.1 New Target: property
Base Type: Record

| Property Name | Type | Description |
|:---|:---|:---|
| **name** (optional) | String | The name that uniquely identifies a property of an actuator. |
| **query_string** (optional) | String | A query string that identifies a single property of an actuator.<br>The syntax of the query string is defined in the actuator profile. |

### 1.2.1 Updated Property Table: OpenC2-Response
Base Type: Record

| ID | Property Name | Type | Description |
|:---|:---|:---|:---|
| 1 | **id** (optional) | Response-ID | ID of the response |
| 2 | **id_ref** (required) | Command-ID | ID of the command that induced this response. |
| 3 | **status** (required) | Status-Code | An integer containing a numerical status code |
| 4 | **status_text** (optional) | String | A free-form string containing human-readable description of the response status |
| 5 | **results** (optional) | Results | Contains the data or extended status information that was requested from an OpenC2 Command |

