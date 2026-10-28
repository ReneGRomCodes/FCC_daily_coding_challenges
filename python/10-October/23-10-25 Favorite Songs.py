"""
Favorite Songs
Remember iPods? The first model came out 24 years ago today, on Oct. 23, 2001.

Given an array of song objects representing your iPod playlist, return an array with the titles of the two most played
songs, with the most played song first.

Each object will have a "title" property (string), and a "plays" property (integer).

1. favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ])
    should return ["Sync or Swim", "Earbud Blues"].
2. favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ])
    should return ["Clickwheel Love", "99 Downloads"].
3. favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ])
    should return ["Song B", "Song C"].
"""

def favorite_songs(playlist: list[dict[str, str | int]]) -> list[str]:
    playlist = sorted(playlist, key=lambda x: x["plays"], reverse=True)[:2]  # Sort playlist by 'plays' entry in dicts
                                                                             # and remove all but the two most played.
    fav_songs: list[str] = [x["title"] for x in playlist]

    return fav_songs


print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))
print(favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]))
print(favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]))
