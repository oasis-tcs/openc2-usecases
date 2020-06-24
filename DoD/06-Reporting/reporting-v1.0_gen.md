<!-- Generated from C:\Users\David\PycharmProjects\jadn-sw\scripts\schema\reporting-v1.0.jadn, Wed Jun 24 10:58:29 2020-->
## Schema
| . | . |
| ---: | :--- |
| **module:** | http://scapstandards.com/monitoring_overlay/0.1 |
| **exports:** | Monitoring-Overlay |

**_Type: Monitoring-Overlay (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **id** | String /uri | 1 | This file |
| 2 | **schema** | String /uri | 1 | Monitoring Overlay schema |
| 3 | **fileVersion** | Integer | 1 | Version of this file (should this be included in id?) |
| 4 | **bindings** | CheckingFile | 1..* | Bindings to content |

**_Type: CheckingFile (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **contentFile** | FileIdentifier | 1 |  |
| 2 | **periods** | Period | 1..* |  |

**_Type: Period (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **when** | Periodicity | 1 |  |
| 2 | **checks** | CheckIdentifier | 1..* |  |

**_Type: Periodicity (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **on_connect** | Condition | 1 |  |
| 2 | **on_change** | Condition | 1 |  |
| 3 | **recurring** | Interval | 1..* | Should this be optional (check only on connection or change)? |

**_Type: Condition (Enumerated)_**

| ID | Name | Description |
| ---: | :--- | :--- |
| 1 | **never** |  |
| 2 | **always** |  |
| 3 | **missed** | Only if a recurring check was missed |

**_Type: Interval (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **monthly** | Monthly | 1 |  |
| 2 | **weekly** | Weekly | 1 |  |
| 3 | **daily** | Daily | 1 |  |
| 4 | **hourly** | Hourly | 1 |  |
| 5 | **minutely** | Minutely | 1 |  |

**_Type: Monthly (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **months** | Integer | 1 | Number of months between checks |
| 2 | **day** | Integer | 1 | Day of month to check |
| 3 | **time** | TimeOfDay | 1..* | Time of day to run the check |

**_Type: Weekly (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **weeks** | Integer | 1 | Number of weeks between checks |
| 2 | **day** | Integer | 1 | Day of week to check: 1=Sunday |
| 3 | **time** | TimeOfDay | 1..* | Time of day to run the check |

**_Type: Daily (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **days** | Integer | 1 | Number of days between checks |
| 2 | **time** | TimeOfDay | 1..* | Time of day to run the check |

**_Type: Hourly (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **hours** | Integer | 1 | Number of hours between checks |
| 2 | **minutes** | Integer | 1..* | Minutes past the hour |

**_Type: Minutely (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **minutes** | Integer | 1 | Number of minutes between checks |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **FileIdentifier** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **CheckIdentifier** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **TimeOfDay** | Integer | Seconds since midnight |
