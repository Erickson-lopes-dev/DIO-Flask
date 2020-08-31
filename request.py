import requests

post = requests.post('http://127.0.0.1:5000/soma/')

print(post.json())