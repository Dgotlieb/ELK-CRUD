import requests
res = requests.delete('http://localhost:9200/my_app/users/1')
if res.ok:
    print(res.json())
