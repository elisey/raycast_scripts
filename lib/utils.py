import os

class Profile:
    WORK = "WORK"
    PERSONAL = "PERSONAL"

def open_browser_old(url: str, profile: Profile) -> None:
    profile_type_to_name = {
        Profile.WORK: "Default",
        Profile.PERSONAL: "Profile 2"
    }
    profile_name = profile_type_to_name[profile]

    command = f'/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --profile-directory="{profile_name}" "{url}"'
    os.system(command)

def open_browser(url: str, profile: Profile) -> None:
    profile_type_to_id = {
        Profile.WORK: "2",
        Profile.PERSONAL: "1"
    }
    profile_id = profile_type_to_id[profile]
    
    command = f'arc-cli select-space {profile_id} && arc-cli new-tab "{url}"'

    os.system(command)

def select_tab(profile: Profile, tab_id: int) -> None:
    profile_type_to_id = {
        Profile.WORK: "2",
        Profile.PERSONAL: "1"
    }
    profile_id = profile_type_to_id[profile]

    command = f'arc-cli select-tab 1 {tab_id}'

    os.system(command)