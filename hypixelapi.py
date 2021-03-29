from config import *
import requests


def get_friends_online():
    ret = {}
    game_types = {}
    person_online = False
    for friend_uuid in FRIEND_UUIDS:
        status = requests.get(f"https://api.hypixel.net/status?key={API_KEY}&uuid={friend_uuid}").json()
        online_status = status["session"]["online"]
        if online_status:
            game_type = status["session"]["gameType"]
            game_types[FRIEND_UUIDS[friend_uuid]] = game_type
        ret[FRIEND_UUIDS[friend_uuid]] = online_status
        if online_status:
            person_online = True
    return ret, person_online, game_types

