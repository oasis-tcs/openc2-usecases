# 1 Phantom action: "delete file"
| organization | Phantom |
|:---|:---|
| action_targets | delete>>file<br>set>>property<br>query>>property |

## 1.1 Action Description
Delete a file from an endpoint

## 1.2 Actuator Description
This app integrates with a Symantec ATP (Advanced Threat Protection) device to implement ingestion, investigative and containment actions

## 1.3 Actuator Properties
There are several properties that affect the behavior of the actuator. These properties are accessible via `query` and `set` actions.

| Property Name | Type | Default | Description |
|:---|:---|:---|:---|
| **poll_now_ingestion_span** | Number | 10 | Limit last n days for 'Poll Now' |
| **first_scheduled_ingestion_span** | Number | 10 | Limit last n days for first scheduled polling |
| **first_scheduled_ingestion_limit** | Number | 20 | Limit last n incidents for first scheduled polling |

## 1.4 Transport Properties
The following is a list of potential transport-related properties.

* `server`: URL
* `client_id`: OAuth client ID
* `client_secret`: OAuth client secret key
* `verify_server_cert`: Verify server certificate

## 1.5 Examples
### 1.5.1 OpenC2 Command/Response
```
{
    "id": "01076931758653239640628182951035",
    "action": "delete",
    "target": {
        "file": {
            "hashes": {
                "sha256": "D8075D370EB24F495C8CFD5CCB81B39F6E5CCA0D5...E871"
            }
        }
    },
    "actuator": {
        "endpoint": {
            "name": "Symantec ATP",
            "actuator_id": "abc123"
        }
    },
    "args": {
        "response_requested": "complete"
    }
}
```

```
{
    "id_ref": "01076931758653239640628182951035",
    "status": 200
}
```

### 1.5.2 Set an actuator property
```
{
    "id": "01076931758653239640628182951035",
    "action": "set",
    "target": {
        "property": {
            "name": "poll_now_ingestion_span"
        }
    },
    "actuator": {
        "endpoint": {
            "name": "Symantec ATP",
            "actuator_id": "abc123"
        }
    },
    "args": {
        "value": 5
    }
}
```

```
{
    "id_ref": "01076931758653239640628182951035",
    "status": 200
}
```

### 1.5.3 Retrieve an actuator property
```
{
    "id": "01076931758653239640628182951036",
    "action": "query",
    "target": {
        "property": {
            "name": "poll_now_ingestion_span"
        }
    },
    "actuator": {
        "endpoint": {
            "name": "Symantec ATP",
            "actuator_id": "abc123"
        }
    }
}
```

```
{
    "id_ref": "01076931758653239640628182951036",
    "status": 200,
    "results": {
        "first_scheduled_ingestion_span": 10
    }
}
```

## 1.6 Phantom Action JSON
```
  {
    "app_name": "Symantec ATP",
    "app_type": "endpoint",
    "app_description": "This app integrates with a Symantec ATP (Advanced Threat Protection) device to implement ingestion, investigative and containment actions",
    "app_configuration": {
      "server": {
        "order": 0,
        "required": true,
        "data_type": "string",
        "description": "URL"
      },
      "client_id": {
        "order": 2,
        "required": true,
        "data_type": "string",
        "description": "OAuth client ID"
      },
      "client_secret": {
        "order": 3,
        "required": true,
        "data_type": "password",
        "description": "OAuth client secret key"
      },
      "verify_server_cert": {
        "order": 1,
        "default": false,
        "required": true,
        "data_type": "boolean",
        "description": "Verify server certificate"
      },
      "poll_now_ingestion_span": {
        "order": 4,
        "default": 10,
        "required": false,
        "data_type": "numeric",
        "description": "Limit last n days for 'Poll Now'"
      },
      "first_scheduled_ingestion_span": {
        "order": 6,
        "default": 10,
        "required": false,
        "data_type": "numeric",
        "description": "Limit last n days for first scheduled polling"
      },
      "first_scheduled_ingestion_limit": {
        "order": 5,
        "default": 20,
        "required": false,
        "data_type": "numeric",
        "description": "Limit last n incidents for first scheduled polling"
      }
    },
    "action_name": "delete file",
    "action_description": "Delete a file from an endpoint",
    "action_parameters": {
      "hash": {
        "order": 0,
        "primary": true,
        "contains": [
          "sha256"
        ],
        "required": true,
        "data_type": "string",
        "description": "Comma separated (',') SHA256 of the files"
      },
      "device_uid": {
        "order": 1,
        "primary": true,
        "contains": [
          "symantecatp target endpoint"
        ],
        "required": true,
        "data_type": "string",
        "description": "Device UID"
      }
    }
  }
```

