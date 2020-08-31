import requests


def test_app_2():
    post = requests.post('http://127.0.0.1:5000/soma/', json={'valores': [10, 40, 10]})
    get = requests.get('http://127.0.0.1:5000/soma/')

    print(get.json())
    print(post.json())


for item in requests.get('http://127.0.0.1:5000/dev/').json()['devs']:
    print(item)

#
# data = {'nome': 'Renan rodrigues',
#         'habilidades': ['python', 'materiaal']}
# # put_dev = requests.put('http://127.0.0.1:5000/dev/2/', json=data)
# # print(put_dev.json())
#
# del_dev = requests.delete('http://127.0.0.1:5000/dev/2/')
# print(del_dev.json())
#
# print(get_dev.json())


# data = {'nome': 'Daniel almeida',
#         'habilidades': ['python', 'materiaal']}
# post_dev = requests.post('http://127.0.0.1:5000/dev/', json=data)
# print(post_dev.json())



