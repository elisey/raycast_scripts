#!/bin/bash

# @raycast.title OK Lets go
# @raycast.description Play OK Lets go

# @raycast.icon images/lets_go.png
# @raycast.mode silent
# @raycast.packageName Misc
# @raycast.schemaVersion 1


current_vol=$(osascript -e 'output volume of (get volume settings)')
osascript -e "set volume output volume 50"
play -q data/okay_lets_go.mp3
osascript -e "set volume output volume $current_vol"
