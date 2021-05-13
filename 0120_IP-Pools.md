# IP-Pools
|- 10.255.0.0/22 (Loopbacks) <br>
&nbsp;&nbsp;&nbsp;|--> 10.255.0.0/24 - Super Spine<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.1.0/24 - Spine<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.2.0/24 - Leaf<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.3.0/24 - Leaf IP Pool Backup<br>
|- 10.255.16.0/22 (Link IPs)<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.16.0/24 - Spines<>Superspines<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.17.0/24 - Spines<>Leafs<br>

## ------------------------------------------------------------------------
## DC1-Loopbacks-10.255.0.0/24 (Super Spine)

### API POST (create)  - Super Spine
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Loopbacks-SuperSpine.json
{
      "id": "ip_dc1_loopbacks_superspine",
      "display_name": "DC1-Lo-SuperSpine-10.255.0.0/24",
      "status": "not_in_use",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.0.0/24"
        }
      ],
      "tags": [
        "DC1"
      ]
}
EOT
```

```bash
curl  -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/ip-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_ip-pools_DC1-Loopbacks-SuperSpine.json
```

### API POST (create)  - Spine
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Loopbacks-Spine.json
{
      "id": "ip_dc1_loopbacks_spine",
      "display_name": "DC1-Lo-Spine-10.255.1.0/24",
      "status": "not_in_use",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.1.0/24"
        }
      ],
      "tags": [
        "DC1"
      ]
}
EOT
```

```bash
curl  -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/ip-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_ip-pools_DC1-Loopbacks-Spine.json
```

### API POST (create)  - Leaf
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Loopbacks-Leaf.json
{
      "id": "ip_dc1_loopbacks_leaf",
      "display_name": "DC1-Lo-Leaf-10.255.2.0/24",
      "status": "not_in_use",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.2.0/24"
        }
      ],
      "tags": [
        "DC1"
      ]
}
EOT
```

```bash
curl  -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/ip-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_ip-pools_DC1-Loopbacks-Leaf.json
```

## ###################################################################################################
## DC1-Links-10.255.16.0/22

### API POST (create) 
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Links.json
{
      "id": "ip_dc1_links",
      "display_name": "DC1-Links-10.255.16.0/22",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.16.0/22"
        }
      ],
      "tags": [
        "DC1"
      ]
}
EOT
```

```bash
curl -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/ip-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_ip-pools_DC1-Links.json
```
