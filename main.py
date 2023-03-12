import json
from datetime import datetime
from hashlib import md5
from jose import jwt
import requests


base_url = "https://api-auth.sandbox.qitech.app"
date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")
method = "POST"
content_type = "application/json"
endpoint = "/test"

headers = {"alg": "ES512", "typ": "JWT"}
body = {"name": "QI Tech"}


api_key = "e48eec43-e77d-4bd9-8452-0a85f679e989"

client_private_key = '''-----BEGIN EC PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,574BB147197491F20131640BDF809372

ypmqJP7NmZ7VdWlbMbu+L0kXkVCgVF58EN8AZdJHy4a7WXuGLrZ+yQHr7/whsuj0
dtTFCanSG504zVsuCsVA4N9jPvVpBFFK3WQFNgRftKiBcWabcjp9t6mN0CTJDELx
zaUhyBP1SGT1KOQ9po1hpKOV7YJdqVIUviV99tZ/o/+yePyrZjd/0/L8WH78lFdz
ZQoPqaNBa+n9zhgCV5VHiD13VPNqmqjLhOmhH7KF0b/mw4D2xZAOWgVp0e1Cvzni
MPbBCaDqoxycIXxI1OymSxtwwdgg0Lrz1Jk93sTzx9A=
-----END EC PRIVATE KEY-----'''

qi_public_key = '''-----BEGIN PUBLIC KEY-----
MIGbMBAGByqGSM49AgEGBSuBBAAjA4GGAAQBuPBRZPmE2dGt9mjQE6XIPphidlRN
rIufCr7ej6jxjDokZY0JN+ORFiAXZLrc2AkVCA0s5P5/ZumlZ+01guxP4e8AqnZU
ALFb0Jl0zfPYy8moa4PHYJ7JzVl4S0QUZBvySLCR919eEo0iCTg/Bhb+ZUxgrG6a
pdOEbvnvlhCCMIgPd4g=
-----END PUBLIC KEY-----'''



encoded_body_token = jwt.encode(claims=body, key=client_private_key, algorithm="ES512")


request_body = {"encoded_body": encoded_body_token}

md5_encode = md5()
md5_encode.update(encoded_body_token.encode())
md5_body = md5_encode.hexdigest()



base_url = "https://api-auth.sandbox.qitech.app"

date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S GMT")

method = "POST"
content_type = "application/json"
endpoint = "/test"


string_to_sign = method + "\n" + md5_body + "\n" + content_type + "\n" + date + "\n" + endpoint


claims = {"sub": api_key, "signature": string_to_sign}
encoded_header_token = jwt.encode(claims=claims, key=client_private_key, algorithm="ES512", headers=headers,)


authorization = "QIT" + " " + api_key + ":" + encoded_header_token
request_header = {"AUTHORIZATION": authorization, "API-CLIENT-KEY": api_key}


url = f"{base_url}{endpoint}"



resp = requests.post(url=url, headers=request_header, json=request_body)
print(resp.json())
