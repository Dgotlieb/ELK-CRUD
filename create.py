import requests
res = requests.post('http://localhost:9200/my_app/users/1', json={"user_name": "john"})
if res.ok:
    print(res.json())
