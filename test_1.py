import requests


def get(token):
    g = requests.get('https://test-stand.gb.ru/api/posts', headers={'X-Auth-Token': token})
    listcont = [i['content'] for i in g.json()['data']]
    return listcont



def test_1(login, text1):
    assert text1 in get(login)
