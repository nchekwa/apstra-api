# Login (auth token)

### bash> create Apstra IP variable
```bash
export apstra_ip=10.10.10.5
```

### bash> create new token 
```bash
curl -k -X POST "https://$apstra_ip/api/user/login" \
  -H  "accept: application/json" \
  -H  "content-type: application/json, Cache-Control:no-cache" \
  -d "{ \"username\":\"admin\", \"password\":\"admin\" }"
> {"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiY3JlYXRlZF9hdCI6IjIwMjEtMDEtMDhUMTk6MjU6MjkuMzIyNDg1IiwidXNlcl9zZXNzaW9uIjoiNTdhMzM1NDAtNjYxMi00OWYyLTllZTAtOWZjZTAwYWU2ZmVhIiwiZXhwIjoxNjEwMjIwMzI5fQ.jZEPBCNHviO10AWaEU7GxWEh33OyetR22qX4cg5dYTI", "id": "2d44e0a1-e3f1-4ed3-ab30-76af1d4fb24d"}
```

### bash> create new token
```bash
export token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiY3JlYXRlZF9hdCI6IjIwMjEtMDEtMDhUMTk6MjU6MjkuMzIyNDg1IiwidXNlcl9zZXNzaW9uIjoiNTdhMzM1NDAtNjYxMi00OWYyLTllZTAtOWZjZTAwYWU2ZmVhIiwiZXhwIjoxNjEwMjIwMzI5fQ.jZEPBCNHviO10AWaEU7GxWEh33OyetR22qX4cg5dYTI
```

### bash> check token value (print token)
```bash
echo $toekn
> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwiY3JlYXRlZF9hdCI6IjIwMjEtMDEtMDhUMTk6MjU6MjkuMzIyNDg1IiwidXNlcl9zZXNzaW9uIjoiNTdhMzM1NDAtNjYxMi00OWYyLTllZTAtOWZjZTAwYWU2ZmVhIiwiZXhwIjoxNjEwMjIwMzI5fQ.jZEPBCNHviO10AWaEU7GxWEh33OyetR22qX4cg5dYTI
```

# APSTRA Authentication Section Config File
*/etc/aos/aos.conf*
```text
[authentication]

# Enable authentication/authorization check. By default
# authentication/authorization is enabled. You can disable it by setting enable
# to 0
enable = 1
# Set token expiration time (in seconds). By default token will be expired
# after 24 hours (86400 seconds).
token_expiration = 86400
```

