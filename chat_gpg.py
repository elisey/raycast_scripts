#!/usr/bin/env python3

# @raycast.title Chat GPG
# @raycast.description Open Chat GPG in browser

# @raycast.icon images/ai.png
# @raycast.mode silent
# @raycast.packageName Google
# @raycast.schemaVersion 1


import sys

from lib.utils import Profile, open_browser

url = "https://chat.openai.com/chat"
open_browser(url, Profile.PERSONAL)
