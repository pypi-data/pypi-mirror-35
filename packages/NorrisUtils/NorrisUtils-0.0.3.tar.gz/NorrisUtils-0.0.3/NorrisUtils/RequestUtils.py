import requests


def commonGet(url, headers=None, cookies=None):
    req = requests.get(url=url, headers=headers, cookies=cookies)
    return req


def commonPost(url, headers=None, cookies=None, data=None):
    req = requests.post(url=url, headers=headers, cookies=cookies, data=data)
    return req
