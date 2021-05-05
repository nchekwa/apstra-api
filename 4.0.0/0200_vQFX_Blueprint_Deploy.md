# Deploy Blueprint Template L3 vQFX


## API POST (create) 
```bash
cat <<EOT > /tmp/deploy_templates_L3-2xvQFX.json
{
  "init_type": "string",
  "design": "string",
  "id": "string",
  "label": "string"
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
