# Create vQFX Interface Map (AOS-12x10-SuperSpine)

![GUI](img/0022.png "Create vQFX Interface Map")

## API POST (create) 
```bash
cat <<EOT > /tmp/design_interface-maps_AOS-12x10-SuperSpine.json
{
  "logical_device_id": "AOS-12x10-SuperSpine",
  "device_profile_id": "Juniper_vQFX",
  "id": "Juniper_vQFX__AOS-12x10-SuperSpine",
  "label": "Juniper vQFX__AOS-12x10-SuperSpine",
  "interfaces": [
    {
      "name": "xe-0/0/0",
      "roles": [
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
        "generic",
        "spine"
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
  -k -X POST "https://$apstra_ip/api/design/interface-maps" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/design_interface-maps_AOS-12x10-SuperSpine.json
```
