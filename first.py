# -*- coding: utf-8 -*-

import requests
import json

base_friend = "http://api.vk.com/method/friends.get?user_id=%d"
base_user = "http://api.vk.com/method/users.get?user_id=%d"


def get_friends(user_id):
    friends = []
    resp = json.loads(requests.get(base_friend % user_id).text)
    if "response" in resp:
        friends = resp["response"]
    return friends


def get_user(user_id):
    return json.loads(requests.get(base_user % user_id).text)


def vk_depth(friend, block):
    print(friend)
    user = get_user(friend)
    file = open("all_users", "a", encoding='utf8')
    file.write(json.dumps(user) + "\n")
    file.close()
    friends = get_friends(friend)
    for friend_of_friend in friends:
        if friend_of_friend not in block:
            block.append(friend_of_friend)
            vk_depth(friend_of_friend, block)


vk_depth(1, [1])
