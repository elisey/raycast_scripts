#!/usr/bin/env python3

# @raycast.title Google Calendar
# @raycast.description Open google calendar in browser

# @raycast.icon images/google-calendar.png
# @raycast.mode silent
# @raycast.packageName Google
# @raycast.schemaVersion 1

# @raycast.argument1 { "type": "text", "placeholder": "personal?", "optional": true }

import sys

from lib.utils import Profile, open_browser

url = "https://calendar.google.com/calendar"

if sys.argv[1] == "":
    open_browser(url, Profile.WORK)
else:
    open_browser(url, Profile.PERSONAL)
