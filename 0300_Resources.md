# ASN
A 4-byte ASN is a 32-bit number.<br>
ANA reserved a block of 94,967,295 ASNs (4200000000 to 4294967294) for private use.<br>
Source: https://www.arin.net/resources/guide/asn/<br>
<br>
Syntax:<br>
42 XXXX YYYY<br>
XXXX = DataCenter ID - DC1=0001<br> 
YYYY = Device ID<br>
<br>
DC1 Example:<br>
ASNs – Suer Spines (ID 4200010010-19)<br>
ASNs – Spines (ID 4200010020-29)<br>
ASNs – Leafs (ID 4200010030-9999)<br>
ASNs - Externals (65000 - 65099)<br>

# IP-Pools
Middle-Size DC require private IP range /21 for IP-Pools<br>
<br> 
DC1 Example:<br>
|- <b>10.255.0.0/21</b> (IP Pool DC1)<br>
|-- <b>10.255.0.0/22</b> (Loopbacks) <br>
&nbsp;&nbsp;&nbsp;|--> 10.255.0.0/24 - Super Spine<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.1.0/24 - Spine<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.2.0/24 - Leaf<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.3.0/24 - Leaf 2nd Backup Pool<br>
|-- <b>10.255.4.0/22</b> (Link IPs)<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.4.0/24 - To Generic Underlay (External)<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.5.0/24 - Spines<>Superspines<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.6.0/24 - Spines<>Leafs<br>
&nbsp;&nbsp;&nbsp;|--> 10.255.7.0/24 - Spines<>Leafs 2nd Backup Pool<br>

# VNI
Avalible Range: 4096 - 16777214<br>

Syntax:<br>
XXXX YY YYYY<br>
XXXX = DataCenter ID - DC1=0001<br> 
YY YYYY = VNI Customer ID<br>

DC1 Example: <br>
VNI CustomerA: 1 00 0001 -> 1000001 <br>
VNI CustomerB: 1 00 0002 -> 1000002 <br>
VNI CustomerC: 1 00 0003 -> 1000003 <br>

<br>
<br>
<br>

## ------------------------------------------------------------------------------------------------
## ASNs – Suer Spines (ID 10-19)
```bash
cat <<EOT > /tmp/resources_asn-pools_DC1-SuperSpines.json
{
      "id": "asn_dc1_superspines",
      "display_name": "DC1-SuperSpines",
      "tags": [
        "DC1"
      ],
      "ranges": [
        {
          "status": "pool_element_available",
          "first": 4200010010,
          "last": 4200010019
        }
      ]
    }
EOT
```

```bash
curl  -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/asn-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_asn-pools_DC1-SuperSpines.json
```


## ASNs – Spines (ID 20-29)
### API POST (create) 
```bash
cat <<EOT > /tmp/resources_asn-pools_DC1-Spines.json
{
      "id": "asn_dc1_spines",
      "display_name": "DC1-Spines",
      "tags": [
        "DC1"
      ],
      "ranges": [
        {
          "status": "pool_element_available",
          "first": 4200010020,
          "last": 4200010029
        }
      ]
    }
EOT
```

```bash
curl  -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/asn-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_asn-pools_DC1-Spines.json
```


## ASNs – Leafs (ID 30-9999)
### API POST (create) 
```bash
cat <<EOT > /tmp/resources_asn-pools_DC1-Leafs.json
{
      "id": "asn_dc1_leafs",
      "display_name": "DC1-Leafs",
      "tags": [
        "DC1"
      ],
      "ranges": [
        {
          "status": "pool_element_available",
          "first": 4200010030,
          "last": 4200019999
        }
      ]
    }
EOT
```

```bash
curl -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/asn-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_asn-pools_DC1-Leafs.json
```



## ASNs - Externals (65000 - 65099)
### API POST (create) 
```bash
cat <<EOT > /tmp/resources_asn-pools_DC1-Externals.json
{
      "id": "asn_dc1_externals",
      "display_name": "DC1-Externals",
      "tags": [
        "DC1"
      ],
      "ranges": [
        {
          "status": "pool_element_available",
          "first": 65000,
          "last": 65099
        }
      ]
    }
EOT
```

```bash
curl -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/resources/asn-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_asn-pools_DC1-Externals.json
```



## ------------------------------------------------------------------------------------------------
## DC1-Loopbacks-10.255.0.0/24 (Super Spine)
### API POST (create)
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

## DC1-Links-10.255.4.0/24 - To Generic Underlay (external)
### API POST (create) 
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Links-To-Generic-Underlay.json
{
      "id": "ip_dc1_links_to_generic_underlay",
      "display_name": "DC1-Links-To-Generic-Underlay-10.255.4.0/24",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.4.0/24"
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
  -d @/tmp/resources_ip-pools_DC1-Links-To-Generic-Underlay.json
```

## DC1-Links-10.255.5.0/24 - Spines<>Superspines
### API POST (create) 
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Spines2Superspines.json
{
      "id": "ip_dc1_links_spines2superspines",
      "display_name": "DC1-Links-Spines2Superspines-10.255.5.0/24",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.5.0/24"
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
  -d @/tmp/resources_ip-pools_DC1-Spines2Superspines.json
```


## DC1-Links-10.255.6.0/24 - Spines<>Leafs
### API POST (create) 
```bash
cat <<EOT > /tmp/resources_ip-pools_DC1-Spines2Leafs.json
{
      "id": "ip_dc1_links_spines2leafs",
      "display_name": "DC1-Links-Spines2Leafs-10.255.6.0/24",
      "subnets": [
        {
          "status": "pool_element_available",
          "network": "10.255.6.0/24"
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
  -d @/tmp/resources_ip-pools_DC1-Spines2Leafs.json
```



## ------------------------------------------------------------------------------------------------
## VNI DC1 (1000000 - 1999999)
### API POST (create)
```bash
cat <<EOT > /tmp/resources_vni-pools_DC1.json
{
  "id": "vni_dc1",
  "display_name": "DC1",
  "ranges": [
    {
      "status": "pool_element_available",
      "first": 100000,
      "last":  199999
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
  -k -X POST "https://$apstra_ip/api/resources/vni-pools" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/resources_vni-pools_DC1.json
```