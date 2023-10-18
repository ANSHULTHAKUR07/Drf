import requests
import json
# try:
#     # data = requests.get('http://127.0.0.1:8000/todourl/user?pk=3')
#     # data = requests.get('http://127.0.0.1:8000/todourl/user')
#     # data = requests.post('http://127.0.0.1:8000/todourl/user',data={"username":"dikashaa","password":"dikshaa123"})

#     # data = requests.post('http://127.0.0.1:8000/todourl/tags',data={"tag_name":"facebook",})
#     # data = requests.get('http://127.0.0.1:8000/todourl/tags?pk=2')

#     # data = requests.post('http://127.0.0.1:8000/todourl/tasks',data={"task_name":"Work on Home page", "task_description":"change style of home ", "task_status":"p","tag":2, "user":2})
#     # data = requests.get('http://127.0.0.1:8000/todourl/tasks?pk=1')

#     # data = requests.post('http://127.0.0.1:8000/todourl/login',data={"username":"shalu","password":"shalu123"})

#     # data = requests.get('http://127.0.0.1:8000/todourl/checkmate', {'id':1})
#     print(data.json())
# except Exception as e:
#     print(e)

import base64

username = base64.b64encode(b'admin:admin')
print(username)

dec = base64.b64decode(username).decode('utf-8')
print(dec)

