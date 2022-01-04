# Deploy Blueprint Deploy


## API POST (create) 
```bash
cat <<EOT > /tmp/deploy_blueprint_deploy_dc1.json
{
  "init_type": "template_reference",
  "template_id": "DC_vQFX_5-Stage",
  "design": "two_stage_l3clos",
  "id": "DC1",
  "label": "DC1"
}
EOT
```

```bash
curl -H "AuthToken: $token" \
  -k -X POST "https://$apstra_ip/api/blueprints" \
  -H  "accept: application/json" \
  -H  "content-type: application/json" \
  -d @/tmp/deploy_blueprint_deploy_dc1.json
```
