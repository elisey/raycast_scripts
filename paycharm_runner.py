#!/usr/bin/env python3

# @raycast.title pycharm
# @raycast.description Open pycharm project

# @raycast.icon images/python-file.png
# @raycast.mode silent
# @raycast.packageName Google
# @raycast.schemaVersion 1

# @raycast.argument1 { "type": "text", "placeholder": "project"}

import sys
import os

from lib.utils import Profile, open_browser

projects = {
    "scp": "~/workspace/project_1",
    "sidecar": "~/workspace/project_2",
}
try:
    path = projects[sys.argv[1]]
except KeyError:
    print("Invalid project name")
    sys.exit(1)

command = f'~/.local/bin/pycharm {path}'
os.system(command)

