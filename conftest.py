#Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, 
# а потом проверяется его наличие на сервере по полю «описание».

#Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/gateway/posts 
# с передачей параметров title, description, content.
import pytest
import requests
import yaml

with open('my.yaml') as f:
    data = yaml.safe_load(f)
    
name = data['user']
passwd = data['pass']
tiltle = data['tiltle']
description = data['description']
content = data['content']

@pytest.fixture()
def login():
    r = requests.post('https://test-stand.gb.ru/gateway/login', data={'username':name,'password':passwd})
    return r.json()['token']
@pytest.fixture()
def newpost():
    r = requests.post('https://test-stand.gb.ru/gateway/posts', data={'tiltle':tiltle,'description':description,'content':content})
    return r.json()['token']
@pytest.fixture()
def text1():
    return 'Fresh jokes'
@pytest.fixture()
def text2():
    return 'new description from Python'