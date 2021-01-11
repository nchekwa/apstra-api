# IP-Pools


## DC1-Loopbacks-10.255.0.0/24 (Spines / Leafs)

### API POST (create) 
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Loopbacks.json
{
      "id": "ip_dc1_loopbacks",
      "display_name": "DC1-Loopbacks-10.255.0.0/24",
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
  -k -X POST "https://10.10.10.5/api/resources/ip-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_ip-pools_DC1-Loopbacks.json
```


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
  -k -X POST "https://10.10.10.5/api/resources/ip-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_ip-pools_DC1-Links.json
```
