import requests

class ApiBroken(Exception):
    pass


def get_uuid_from_username(username):
    rq = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{username}')
    if rq.status_code == 200:
        json = rq.json()
        return json['id']
    else:
        raise ApiBroken

