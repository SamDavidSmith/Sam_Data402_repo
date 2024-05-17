import json

import requests

post_code_req = requests.get("https://api.postcodes.io/postcodes/pr85dj")
# print(post_code_req)
# print(f"Status code: {post_code_req.status_code}")
# print(f"Headers: {post_code_req.headers}")
# print(f"Content: {post_code_req.content}")
# print(f"JSON: {post_code_req.json()}")
# print(f"JSON data type: {type(post_code_req.json())}")

json_body = json.dumps({"postcodes": ["PR3 0SG", "M45 6GN", "EX165BL"]})
headers = {"Content-Type": "application/json"}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers = headers, data = json_body)

print(post_multi_req.json())