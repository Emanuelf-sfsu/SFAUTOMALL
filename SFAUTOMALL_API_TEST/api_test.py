import requests
import json
expected=[
      {
            "url": "http://127.0.0.1:5000/vehicle",
            "make": "Ford",
            "model": "Escort",
            "year": 2020,
            "value": 12000,
            "buyer": "NA",
            "repair": "null",
            "District_id": 1
      },
      {
            "url": "http://127.0.0.1:5000/vehicle",
            "make": "Toyota",
            "model": "Camery",
            "year": 2022,
            "value": 30000,
            "buyer": "NA",
            "repair": "null",
            "District_id": 2
      },
      {
            "url": "http://127.0.0.1:5000/vehicle",
            "make": "Ford",
            "model": "1500",
            "year": 2002,
            "value": 100,
            "buyer": "Jack",
            "repair": 1,
            "District_id": 1
      }
]
def test_post_headers_body_json():
    url = 'http://127.0.0.1:5000/vehicle'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # body
    payload={}

    # Conver dict to json string by json.dumps() for body data.
    resp = requests.get(url, headers=headers, data=json.dumps(payload,indent=4))
    
    # Validate response headers and body content, e.g. status code
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body[0] == expected
    # response = requests.request("GET", url, headers=headers, data=payload)
    print(resp.text)
