# Blueprint Deploy

![GUI](img/0500.png "Blueprint Commit-Deploy")


## GET current DIFF between stage and current deply 
```bash
export blueprint_id=DC1
curl -H "AuthToken: $token" \
  -s -k -X GET "https://$apstra_ip/api/blueprints/$blueprint_id/diff" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" | jq .
```

## Get current blueprint version
```bash
export blueprint_version=`curl -H "AuthToken: $token" \
  -s -k -X GET "https://$apstra_ip/api/blueprints/$blueprint_id" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/deploy_blueprint.json | jq .version`

cat <<EOF > /tmp/deploy_blueprint.json
{
  "version": $blueprint_version,
  "descripton": "Commit Version: $blueprint_version"
}
EOF

cat /tmp/deploy_blueprint.json
```

## Deploy
```bash
curl -H "AuthToken: $token" \
  -s -k -X PUT "https://$apstra_ip/api/blueprints/$blueprint_id/deploy" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/deploy_blueprint.json | jq .
```

## Check Deploy Status
```bash
curl -H "AuthToken: $token" \
  -s -k -X GET "https://$apstra_ip/api/blueprints/$blueprint_id/deploy" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" | jq .
```