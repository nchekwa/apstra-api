# Blueprint Update Resources

![GUI](img/0400.png "Blueprint Update Resources")

ASNs - Superspines - [superspine_asns]<br>
ASNs - Spines - [spine_asns]<br>
ASNs - Leafs - [leaf_asns]<br>
Loopback IPs - Superspines - [superspine_loopback_ips]<br>
Loopback IPs - Spines - [spine_loopback_ips]<br>
Loopback IPs - Leafs - [leaf_loopback_ips]<br>
Link IPs - Spines<>Superspines - [spine_superspine_link_ips]<br>
Link IPs - Spines<>Leafs - [spine_leaf_link_ips]<br>
<br>

Set variable with name of Blueprint ID
```bash
export blueprint_id=DC1
```

# ASNs
## ASNs - Superspines - [superspine_asns]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/asn/superspine_asns" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids":["asn_dc1_superspines"]}'
```

## ASNs - Spines - [spine_asns]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/asn/spine_asns" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["asn_dc1_spines"] }'
```

## ASNs - Leafs - [leaf_asns]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/asn/leaf_asns" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["asn_dc1_leafs"] }'
```



# Loopback IPs
## Loopback IPs - Superspines - [superspine_loopback_ips]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/ip/superspine_loopback_ips" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["ip_dc1_loopbacks_superspines"] }'
```

## Loopback IPs - Spines - [spine_loopback_ips]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/ip/spine_loopback_ips" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["ip_dc1_loopbacks_spines"] }'
```


## Loopback IPs - Leafs - [leaf_loopback_ips]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/ip/leaf_loopback_ips" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["ip_dc1_loopbacks_leafs"] }'
```


# Link IPs
## Link IPs - Spines<>Superspines - [spine_superspine_link_ips]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/ip/spine_superspine_link_ips" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["ip_dc1_links_spines2superspines"] }'
```

## Link IPs - Spines<>Leafs - [spine_leaf_link_ips]
```bash
curl -s -H "AuthToken: $token" \
  -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/resource_groups/ip/spine_leaf_link_ips" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d  '{"pool_ids": ["ip_dc1_links_spines2leafs"] }'
```

