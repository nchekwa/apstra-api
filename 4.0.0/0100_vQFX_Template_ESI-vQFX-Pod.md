# Create Blueprint Template L3 vQFX

![GUI](img/0100.png "Create Blueprint Template ESI vQFX Pod")

## API POST (create) 
```bash
cat <<EOT > /tmp/design_templates_ESI-vQFX-Pod.json
{
  "external_routing_policy": {
    "export_policy": {
      "spine_leaf_links": true,
      "l3edge_server_links": true,
      "l2edge_subnets": true,
      "static_routes": false,
      "loopbacks": true
    },
    "import_policy": "default_only",
    "expect_default_ipv6_route": true,
    "expect_default_ipv4_route": true,
    "extra_export_routes": [],
    "extra_import_routes": [],
    "aggregate_prefixes": [],
    "label": "Default_immutable"
  },
  "display_name": "ESI vQFX Pod",
  "virtual_network_policy": {
    "overlay_control_protocol": "evpn"
  },
  "fabric_addressing_policy": {
    "spine_leaf_links": "ipv4",
    "spine_superspine_links": "ipv4"
  },
  "spine": {
    "count": 2,
    "link_per_superspine_count": 1,
    "tags": [],
    "logical_device": {
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
              "count": 10,
              "speed": {
                "unit": "G",
                "value": 10
              },
              "roles": [
                "superspine",
                "leaf"
              ]
            },
            {
              "count": 2,
              "speed": {
                "unit": "G",
                "value": 10
              },
              "roles": [
                "superspine",
                "leaf",
                "generic"
              ]
            }
          ]
        }
      ],
      "display_name": "AOS-12x10-Spine",
      "id": "AOS-12x10-Spine"
    },
    "link_per_superspine_speed": {
      "unit": "G",
      "value": 10
    }
  },
  "created_at": "2021-05-07T15:29:43.816087Z",
  "rack_type_counts": [
    {
      "rack_type_id": "ESI_vQFX",
      "count": 1
    }
  ],
  "dhcp_service_intent": {
    "active": true
  },
  "last_modified_at": "2021-05-12T13:49:27.415167Z",
  "rack_types": [
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
          "label": "leaf",
          "mlag_vlan_id": 0,
          "leaf_leaf_l3_link_port_channel_id": 0
        }
      ],
      "access_switches": [],
      "id": "ESI_vQFX",
      "display_name": "ESI vQFX",
      "fabric_connectivity_design": "l3clos",
      "created_at": "1970-01-01T00:00:00.000000Z",
      "last_modified_at": "2021-05-12T13:39:31.542278Z"
    }
  ],
  "capability": "pod",
  "asn_allocation_policy": {
    "spine_asn_scheme": "single"
  },
  "type": "rack_based",
  "id": "ESI_vQFX_Pod"
}
EOT
```

```bash
curl -s -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/design/templates" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/design_templates_ESI-vQFX-Pod.json
```
