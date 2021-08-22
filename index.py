import os
import requests


def unsplash(search_key):

    url = f'https://unsplash.com/napi/search?query={search_key}&per_page=20'

    res = requests.get(url)
    data = res.json()
    for links in data['photos']['results']:
        id = links['id']
        image = links['urls']['thumb']

        # download images
        with open(f"{id}.jpg", "wb") as f:
            f.write(requests.get(image).content)


key = input('search: ')
unsplash(key)
