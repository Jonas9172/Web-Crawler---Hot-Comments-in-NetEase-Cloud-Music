import requests
import json


def get_comments(url):

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Referer': 'https://music.163.com/song?id=2051548110',
 }

    params = "2N+/96nVqnwZMKaCcacAUaof9J3JT877ZPUS517BtEkOEV9OVV1bwu6Xr9xA7v3EXj8/G9kay8gnDBUNA5SDUSIVtaFFiuYS0ZxGUAR8ko/c4yFdj5M6IXgADZKBWRauL/7p/lKc6lmwkhv+C2NaufaizkeglyvXe18oH0alPfldURR1Z+RjwAU/xkw7HbblLj+w7pjK90N8YWd97ueKti3oo5n9p5sHTuEZBhJ/BQz889G+3osbOoPTlXBhcIKIr0+3K+jRWOsMV+dyYpUCgIostvDxDnI94ZKiffcb0kM="
    encSecKey = "31576c7202b88b7c0bc477814b344d46dd27e7eed4630e3d6e83840d69eedca1182c1942ea9c5126b096b9868e07041a7ac7798582a419f63b206c3358e4890da24388b2f4c603424f5b30775639e5cb5b755c7b873ba5cbef0609aa99d912ccdc3e8aeae361000be1814e8bd7a40e1344b3692b97b8807632fc83fadd10635a"

    data = {
        "params": params,
        "encSecKey": encSecKey
    }

    target_url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
    res = requests.post(target_url, headers=headers, data=data)

    return res


def get_hotcomments(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['data']['hotComments']
    with open('hot_comments.txt', 'w', encoding='utf-8') as file:
        for each in hot_comments:
            file.write(each['user']['nickname'] + ':\n')
            file.write(each['content'] + '\n\n')


if __name__ == '__main__':
    url = input("Link: ")
    res = get_comments(url)
    get_hotcomments(res)