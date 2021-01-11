# Create vQFX Interface Map (AOS-12x10-Spine)

![GUI](img/0020.png "Create vQFX Interface Map")

## API POST (create) 
```bash
cat <<EOT > /tmp/design_interface-maps_AOS-12x10-Spine.json
{
      "logical_device_id": "AOS-12x10-Spine",
      "device_profile_id": "Juniper_vQFX",
      "id": "Juniper_vQFX__AOS-12x10-Spine",
      "label": "Juniper_vQFX__AOS-12x10-Spine",
      "interfaces": [
        {
          "name": "xe-0/0/0",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            1,
            1,
            1,
            1,
            1
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 1,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/1",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            2,
            1,
            1,
            1,
            2
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 2,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/2",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            3,
            1,
            1,
            1,
            3
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 3,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/3",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            4,
            1,
            1,
            1,
            4
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 4,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/4",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            5,
            1,
            1,
            1,
            5
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 5,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/5",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            6,
            1,
            1,
            1,
            6
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 6,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/6",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            7,
            1,
            1,
            1,
            7
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 7,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/7",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            8,
            1,
            1,
            1,
            8
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 8,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/8",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            9,
            1,
            1,
            1,
            9
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 9,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/9",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            10,
            1,
            1,
            1,
            10
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 10,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/10",
          "roles": [
            "superspine",
            "leaf"
          ],
          "mapping": [
            11,
            1,
            1,
            1,
            11
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 11,
          "speed": {
            "unit": "G",
            "value": 10
          }
        },
        {
          "name": "xe-0/0/11",
          "roles": [
            "superspine",
            "leaf",
            "external_router"
          ],
          "mapping": [
            12,
            1,
            1,
            1,
            12
          ],
          "state": "active",
          "setting": {
            "param": "{\"interface\": {\"speed\": \"\"}, \"global\": {\"speed\": \"\"}}"
          },
          "position": 12,
          "speed": {
            "unit": "G",
            "value": 10
          }
        }
      ]
    }
EOT
```

```bash
curl -H "AuthToken: $token" \
  -k -X POST "https://10.10.10.5/api/design/interface-maps" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/design_interface-maps_AOS-12x10-Spine.json
```
