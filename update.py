import requests
res = requests.put('http://localhost:9200/my_app/users/1', json={"user_name": "jack"})
if res.ok:
    print(res.json())
