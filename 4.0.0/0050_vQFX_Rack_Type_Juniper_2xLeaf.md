# Create Rack Type Juniper 2xLeaf vQFX 12 ports

![GUI](img/0050.png "Create Rack Type Juniper 2xLeaf vQFX 12 ports (ESI Mode)")

## API POST (create) 
```bash
cat <<EOT > /tmp/design_rack-types_L3-2xvQFX.json
{
  "description": "",
  "tags": [],
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
                "generic",
                "spine"
              ]
            },
            {
              "count": 8,
              "speed": {
                "unit": "G",
                "value": 10
              },
              "roles": [
                "generic"
              ]
            }
          ]
        }
      ],
      "display_name": "AOS-12x10-Leaf",
      "id": "AOS-12x10-Leaf"
    }
  ],
  "generic_systems": [],
  "servers": [],
  "leafs": [
    {
      "leaf_leaf_l3_link_speed": null,
      "redundancy_protocol": "esi",
      "leaf_leaf_link_port_channel_id": 0,
      "leaf_leaf_l3_link_count": 0,
      "logical_device": "AOS-12x10-Leaf",
      "leaf_leaf_link_speed": null,
      "link_per_spine_count": 1,
      "leaf_leaf_link_count": 0,
      "tags": [],
      "link_per_spine_speed": {
        "unit": "G",
        "value": 10
      },
      "label": "vQFX",
      "mlag_vlan_id": 0,
      "leaf_leaf_l3_link_port_channel_id": 0
    }
  ],
  "access_switches": [],
  "id": "L3-2xvQFX",
  "display_name": "L3-2xvQFX",
  "fabric_connectivity_design": "l3clos"
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
