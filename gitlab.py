#!/usr/bin/env python3

# How to use this script?
# It's a template which needs further setup. Duplicate the file,
# remove `.template.` from the filename and set an Personal access token as
# well as the GitLab instance url if it is not gitlab.com in gitlabconfig.py
# You need to copy gitlabconfig.py and gitlabhelper.py next to the script command
# otherwise it won't work. gitlabconfig.py and gitlabhelper.py are shared between
# all gitlab script commands.
#
# API: https://docs.gitlab.com/ee/api


# Parameters

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title gitlab mrs
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.packageName GitLab
# @raycast.icon images/pipeline.png

# @raycast.description Show my merge requests from GitLab


from lib.gitlab import GitlabClient, get_gitlab_token

gitlab_token = get_gitlab_token()
client = GitlabClient(gitlab_token, "<gitlab_client_name>")

mrs = client.get_mrs()
for mr in mrs:
    print(f"{mr.pipeline_status.to_view()} - {mr.title}")
    print(mr.web_url)

