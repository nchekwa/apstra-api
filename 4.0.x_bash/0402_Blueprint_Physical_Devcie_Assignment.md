# Blueprint Physical Devcie Assignment

![GUI](img/0402.png "Blueprint Physical Devcie Assignment")

Set variable with name of Blueprint ID
```bash
export blueprint_id=DC1
```


## Print Device System IDs
```bash
curl -s -H "AuthToken: $token" \
  -k -X GET "https://$apstra_ip/api/blueprints/$blueprint_id/cabling-map" \
  -H  "accept: application/json" \
  -H  "content-type: application/json"  | jq -r '.links[].endpoints[].system | .id +" "+ (.role) +" " + (.label)' | column |  sort | uniq | sort -k3 > /tmp/cabling_map.csv
```

## Update Device Profile Interface Map Assignments
```bash
declare -A device_mapping
device_mapping["sspine001_1"]="500010100000"
device_mapping["spine001_001_1"]="500020200000"
device_mapping["spine001_001_2"]="500021210000"
device_mapping["leaf001_001_1"]="500030300000"
device_mapping["leaf001_001_2"]="500031310000"

cabling_map_file="/tmp/cabling_map.csv"
while IFS=$' ' read -r system_id role system_name; do
  curl -s -H "AuthToken: $token" \
    -k -X PATCH "https://$apstra_ip/api/blueprints/$blueprint_id/nodes/${system_id}" \
    -H  "accept: application/json" \
    -H  "content-type: application/json" \
    -d  '{"system_id":"'${device_mapping[${system_name}]}'", "deploy_mode":"deploy"}'
done < "$cabling_map_file"
```



```bash
curl -s -H "AuthToken: $token" \
  -k -X GET "https://$apstra_ip/api/blueprints/$blueprint_id/nodes" \
  -H  "accept: application/json" \
  -H  "content-type: application/json"  | jq .
```