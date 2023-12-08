import requests
import json


def get_comments():

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0',
        'Referer': 'https://music.163.com/song?id=2028308226',
 }

    params = "57hpWVX0K6E/KMdd9rXkExGZUuLmazvCrZ/Bx/i4/QZzijnB6yyj4LXOvMKXQLuPeCRhEVlbsIASaihmFpCaLpSxXBfetD6lSO99xZOFCgDmUE5V5ERxDYMzGNJNGasTzKOzrwCjpWt3JBcXhDt6fgCgHNHmz/TvTxHJHFqrOXZowb6De//e+5S5vsutaTdzOI9FCiZmf86cKlgeiUWQD5RpiF48U7zpOZydCSesyC0CgkJgsu9+pduh+iGL+AqZhgSodb+HEzSjmTABcWfuQgL6fNN6OT4gJWOAKcaijtg="
    encSecKey = "b38e40c2d10fe9e2a51bfde5c05f37ee7d2e2bf10d3410ab9820659c830744830ffe2753d52d949bd68f9d34da17fd85cef7df2cb995f3b54e543af11f72076b3a86e44fd42641530dae2b54cfb39124d57d80fa0f7bf59ed8f99df81c0267d1650fcbce9e16e0b2b63f90fd260451339bcf27e0c872afecbef7bcb0288e75ab"

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
    res = get_comments()
    get_hotcomments(res)
