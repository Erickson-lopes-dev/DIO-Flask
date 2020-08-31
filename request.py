import requests

post = requests.post('http://127.0.0.1:5000/soma/', json={'valores': [10, 40, 10]})
get = requests.get('http://127.0.0.1:5000/soma/')

print(get.json())
print(post.json())

