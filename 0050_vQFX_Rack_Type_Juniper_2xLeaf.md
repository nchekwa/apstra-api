# Create Rack Type Juniper 2xLeaf vQFX 12 ports

![GUI](img/0050.png "Create Rack Type Juniper 2xLeaf vQFX 12 ports")

## API POST (create) 
```bash
cat <<EOT > /tmp/design_rack-types_L3-2xvQFX.json
{
      "display_name": "L3 2xvQFX",
      "id": "L3_2xvQFX",
      "description": "",
      "leafs": [
        {
          "external_router_links": [],
          "external_router_facing": false,
          "leaf_leaf_l3_link_speed": null,
          "redundancy_protocol": null,
          "leaf_leaf_link_port_channel_id": 0,
          "leaf_leaf_l3_link_count": 0,
          "logical_device": "AOS-12x10-Leaf",
          "leaf_leaf_link_speed": null,
          "link_per_spine_count": 1,
          "leaf_leaf_link_count": 0,
          "link_per_spine_speed": {
            "unit": "G",
            "value": 10
          },
          "label": "leaf1",
          "leaf_leaf_l3_link_port_channel_id": 0
        },
        {
          "external_router_links": [],
          "external_router_facing": false,
          "leaf_leaf_l3_link_speed": null,
          "redundancy_protocol": null,
          "leaf_leaf_link_port_channel_id": 0,
          "leaf_leaf_l3_link_count": 0,
          "logical_device": "AOS-12x10-Leaf",
          "leaf_leaf_link_speed": null,
          "link_per_spine_count": 1,
          "leaf_leaf_link_count": 0,
          "link_per_spine_speed": {
            "unit": "G",
            "value": 10
          },
          "label": "leaf2",
          "leaf_leaf_l3_link_port_channel_id": 0
        }
      ],
      "logical_devices": [
        {
          "panels": [
            {
              "panel_layout": {
                "row_count": 1,
                "column_count": 12
              },
              "port_indexing": {
                "order": "T-B, L-R",
                "start_index": 1,
                "schema": "absolute"
              },
              "port_groups": [
                {
                  "count": 4,
                  "speed": {
                    "unit": "G",
                    "value": 10
                  },
                  "roles": [
                    "spine"
                  ]
                },
                {
                  "count": 7,
                  "speed": {
                    "unit": "G",
                    "value": 10
                  },
                  "roles": [
                    "l2_server",
                    "access",
                    "l3_server"
                  ]
                },
                {
                  "count": 1,
                  "speed": {
                    "unit": "G",
                    "value": 10
                  },
                  "roles": [
                    "peer",
                    "l2_server",
                    "access",
                    "l3_server",
                    "external_router"
                  ]
                }
              ]
            }
          ],
          "display_name": "AOS-12x10-Leaf",
          "id": "AOS-12x10-Leaf"
        }
      ],
      "access_switches": [],
      "servers": []
    }
EOT
```

```bash
curl  -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/design/rack-types" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/design_rack-types_L3-2xvQFX.json
```
