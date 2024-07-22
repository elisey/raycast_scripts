#!/usr/bin/env python3

# @raycast.title Yandex Music
# @raycast.description Open yandex music in browser

# @raycast.icon images/music.png
# @raycast.mode silent
# @raycast.packageName Google
# @raycast.schemaVersion 1

from lib.utils import Profile, open_browser

url = "https://music.yandex.ru/"

open_browser(url, Profile.PERSONAL)
