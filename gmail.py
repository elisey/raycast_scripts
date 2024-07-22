#!/usr/bin/env python3

# @raycast.title GMail
# @raycast.description Open google calendar in browser

# @raycast.icon images/gmail.png
# @raycast.mode silent
# @raycast.packageName Google
# @raycast.schemaVersion 1

# @raycast.argument1 { "type": "text", "placeholder": "personal?", "optional": true }

import sys

from lib.utils import Profile, open_browser, select_tab

url = "https://gmail.com"

if sys.argv[1] == "":
    #open_browser(url, Profile.WORK)
    select_tab(Profile.WORK, 6)
else:
    select_tab(Profile.PERSONAL, 7)

