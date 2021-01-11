# Create Blueprint Template L3 vQFX

![GUI](img/0100.png "Create Blueprint Template L3 vQFX")

## API POST (create) 
```bash
cat <<EOT > /tmp/design_templates_L3-2xvQFX.json
{
      "type": "rack_based",
      "id": "template_L3_vQFX",
      "display_name": "L3 vQFX",
      "external_routing_policy": {
        "export_policy": {
          "all_routes": true,
          "spine_leaf_links": false,
          "l3edge_server_links": true,
          "l2edge_subnets": true,
          "loopbacks": true
        },
        "extra_export_routes": [],
        "extra_import_routes": [],
        "import_policy": "all",
        "aggregate_prefixes": []
      },
      "virtual_network_policy": {
        "overlay_control_protocol": "evpn"
      },
      "fabric_addressing_policy": {
        "spine_leaf_links": "ipv4",
        "spine_superspine_links": "ipv4"
      },
      "spine": {
        "count": 2,
        "external_link_speed": null,
        "link_per_superspine_count": 1,
        "link_per_superspine_speed": {
          "unit": "G",
          "value": 10
        },
        "external_links_per_node": 0,
        "external_facing_node_count": 0,
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
                  "count": 11,
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
                  "count": 1,
                  "speed": {
                    "unit": "G",
                    "value": 10
                  },
                  "roles": [
                    "superspine",
                    "leaf",
                    "external_router"
                  ]
                }
              ]
            }
          ],
          "display_name": "AOS-12x10-Spine",
          "id": "AOS-12x10-Spine"
        },
        "external_link_count": 0
      },
      "rack_type_counts": [
        {
          "rack_type_id": "L3_2xvQFX",
          "count": 2
        }
      ],
      "dhcp_service_intent": {
        "active": true
      },
      "rack_types": [
        {
          "created_at": "1970-01-01T00:00:00.000000Z",
          "display_name": "L3 2xvQFX",
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
          "id": "L3_2xvQFX",
          "servers": []
        }
      ],
      "asn_allocation_policy": {
        "spine_asn_scheme": "distinct"
      }
    }
EOT

```

```bash
curl -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/design/templates" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/design_templates_L3-2xvQFX.json
```
