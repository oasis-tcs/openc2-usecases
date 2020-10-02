## Schema
| . | . |
| ---: | :--- |
| **package:** | https://scap.org/edc-prototype/v0.1 |
| **exports:** | Assessment-Instructions, Cancel-Assessment, Assessment-Ack, Collection-Request, Collection-Results, Query, Results, Store-Assessment-Info |

**_Type: Assessment-Instructions (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **content** | Content | 1 | with IDs |
| 2 | **targeting** | Targeting | 1 |  |
| 3 | **oldest** | Oldest-Valid-Results | 1 |  |
| 4 | **latest** | Latest-Return | 1 |  |
| 5 | **get_fresh** | Boolean | 1 |  |
| 6 | **method** | PCE-Filters | 1 |  |
| 7 | **formats** | Format-Filters | 1 |  |
| 8 | **params** | Collection-Parameters | 1 |  |
| 9 | **requestor** | Requestor-ID | 1 |  |

**_Type: Cancel-Assessment (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **transaction** | Transaction-ID | 1 |  |
| 2 | **requestor** | Requestor-ID | 1 |  |

**_Type: Assessment-Ack (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **transaction** | Transaction-ID | 1 |  |

**_Type: Store-Assessment-Info (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **info** | Assessment-Info | 1 | Is this same as 15 report results? |
| 2 | **requestor** | Requestor-ID | 1 |  |

**_Type: Query (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **query** | Query-Info | 1 |  |
| 2 | **query_id** | Query-ID | 1 |  |
| 3 | **requestor** | Requestor-ID | 1 |  |

**_Type: Results (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **results** | Results-Info | 1 |  |
| 2 | **query_id** | Query-ID | 1 |  |
| 3 | **requestor** | Requestor-ID | 1 |  |

**_Type: Query-Info (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **applicability** | Applicability | 1 | 4 |
| 2 | **prior** | Prior-Query-ID | 1 | 6 |
| 3 | **collectors** | Collectors | 1 | 9 |
| 4 | **content** | Content-IDs | 1 | 12 |

**_Type: Results-Info (Choice)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **applicability** | Applicability-Results | 1 | 5 |
| 2 | **prior** | Prior-Results | 1 | 7 |
| 3 | **collectors** | Collectors-Results | 1 | 10 |
| 4 | **content** | Content-Results | 1 | 13 |

**_Type: Collection-Request (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **content_ids** | Content-IDs | 1 |  |
| 2 | **target_ids** | Target-IDs | 1 |  |
| 3 | **latest_return** | Latest-Return | 1 |  |
| 4 | **method** | Collection-Method | 1 | PCE filters |
| 5 | **formats** | Format-Filters | 1 |  |
| 6 | **params** | Collection-Parameters | 1 |  |
| 7 | **transaction** | Transaction-ID | 1 |  |
| 8 | **requestor** | Requestor-ID | 1 |  |

**_Type: Collection-Results (Record)_**

| ID | Name | Type | # | Description |
| ---: | :--- | :--- | ---: | :--- |
| 1 | **assessment** | Assessment | 1 |  |
| 2 | **transaction** | Transaction-ID | 1 |  |
| 3 | **requestor** | Requestor-ID | 1 |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Transaction-ID** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Requestor-ID** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Query-ID** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Content** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Targeting** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Oldest-Valid-Results** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Latest-Return** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **PCE-Filters** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Format-Filters** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Collection-Parameters** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Collection-Method** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Assessment-Info** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Applicability** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Prior-Query-ID** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Collectors** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Content-IDs** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Applicability-Results** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Prior-Results** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Collectors-Results** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Content-Results** | String |  |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Assessment** | String | timestamp, PCE make/model, Target-IDs, etc |


| Type Name | Type Definition | Description |
| :--- | :--- | :--- |
| **Target-IDs** | String |  |
