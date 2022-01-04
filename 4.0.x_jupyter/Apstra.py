import yaml
import requests
import urllib3
import json
import sys
import time
from http.client import responses
from pprint import pprint

class Apstra():
    def __init__(self, inventory) -> None:
        urllib3.disable_warnings()

        self.inventory = inventory
        self.http = urllib3.HTTPSConnectionPool(inventory["aos_server"]["host"], port=inventory["aos_server"]["port"], cert_reqs='CERT_NONE', assert_hostname=False)

        if inventory["aos_server"].get("token"):
            self.token = inventory["aos_server"]['token']
            self.json_token_header = urllib3.response.HTTPHeaderDict({"Content-Type": "application/json", "AuthToken": self.token})
        else:
            self.json_header = urllib3.response.HTTPHeaderDict({"Content-Type": "application/json"})
            self.auth()
            self.json_token_header = urllib3.response.HTTPHeaderDict({"Content-Type": "application/json", "AuthToken": self.token})
    
    # GET
    def http_get(self, path, expected=None) -> urllib3.response.HTTPResponse:
        print(f"=>= GET {path}")
        resp = self.http.request('GET', path, headers=self.json_token_header)
        code_desc = responses[resp.status]
        if expected:
            print(f"=<= Status (expect {expected}): {resp.status} {code_desc}")
            if resp.status != expected:
                print("=<= Body: ")
                obj = json.loads(resp.data.decode())
                print(json.dumps(obj, indent=4))
        else:
            print(f"=<= Status: {resp.status} {code_desc}")
        return resp

    # DELETE
    def http_delete(self, path, expected=None) -> urllib3.response.HTTPResponse:
        print(f"=>= DELETE {path}")
        resp = self.http.request('DELETE', path, headers=self.json_token_header)
        code_desc = responses[resp.status]
        if expected:
            print(f"=<= Status (expect {expected}): {resp.status} {code_desc}")
            if resp.status != expected:
                print("=<= Body: ")
                obj = json.loads(resp.data.decode())
                print(json.dumps(obj, indent=4))
        else:
            print(f"=<= Status: {resp.status} {code_desc}")
        return resp

    # POST
    def http_post(self, path, data, headers=None, expected=None) -> urllib3.response.HTTPResponse:
        if not headers:
            headers = self.json_token_header
        print(f"=>= POST {path}\n=>= DATA: ")
        pprint(data)
        resp = self.http.request('POST', path, body=json.dumps(data), headers=headers)
        code_desc = responses[resp.status]
        if expected:
            print(f"=<= Status (expect {expected}): {resp.status} {code_desc}")
            if resp.status != expected:
                print("=<= Body: ")
                obj = json.loads(resp.data.decode())
                print(json.dumps(obj, indent=4))
        else:
            print(f"=<= Status: {resp.status} {code_desc}")
        return resp

    # PUT
    def http_put(self, path, data, headers=None, expected=None) -> urllib3.response.HTTPResponse:
        print(f"=>= PUT {path}\n=>= DATA: ")
        pprint(data)
        if not headers:
            headers = self.json_token_header
        resp = self.http.request('PUT', path, body=json.dumps(data), headers=headers)
        if expected:
            print(f"=<= Status (expect {expected}): {resp.status}")
            if resp.status != expected:
                print("=<= Body: ")
                obj = json.loads(resp.data.decode())
                print(json.dumps(obj, indent=4))
        else:
            print(f"=<= Status: {resp.status}")
        return resp

    # PATCH
    def http_patch(self, path, data, headers=None, expected=None) -> urllib3.response.HTTPResponse:
        print(f"=>= PATCH {path}\n=>= DATA: ")
        pprint(data)
        if not headers:
            headers = self.json_token_header
        resp = self.http.request('PATCH', path, body=json.dumps(data), headers=headers)
        if expected:
            print(f"=<= Status (expect {expected}): {resp.status}")
            if resp.status != expected:
                print("=<= Body: ")
                obj = json.loads(resp.data.decode())
                print(json.dumps(obj, indent=4))
        else:
            print(f"=<= Status: {resp.status}")
        return resp

    def get_token(self):
        return self.token


    def search(self, path, search_key, search_value):
        resp = self.http_get(path, expected=200)
        resp_body = json.loads(resp.data.decode())
        if type(resp_body['items']) is list:
            for j in resp_body['items']:
                if j[search_key] == search_value:
                    return(j)
        if type(resp_body['items']) is dict:
            for j in resp_body['items'].items():
                if type(j) is tuple:
                    for item in j:
                        if type(item) is dict:
                            if item.get(search_key) == search_value:
                                return(item)
        return False
        
    def auth(self) -> None:
        auth_url = "/api/aaa/login"
        auth_spec = {
            "username": self.inventory["aos_server"]["username"],
            "password": self.inventory["aos_server"]["password"]
        }
        resp = self.http_post( auth_url, auth_spec, headers=self.json_header, expected=201)
        self.token = json.loads(resp.data)["token"]
        print(f"=<= Token: {self.token}")
    
    def commit(self, bp_id, description='commit by script') -> urllib3.response.HTTPResponse:
        # get revision id
        revision_url = f"/api/blueprints/{bp_id}/revisions"
        revision_data = json.loads(self.http_get(revision_url,expected=200).data)
        revision_id = int(revision_data["items"][-1]["revision_id"]) + 10

        commit_url = f"/api/blueprints/{bp_id}/deploy?async=full"
        commit_data = {
            "version": revision_id,
            "description": description
        }
        resp = self.http_put(commit_url, commit_data, expected=202)
        return resp