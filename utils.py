# utils.py

import requests
from config import OKTA_DOMAIN, OKTA_API_TOKEN

headers = {
    "Authorization": f"SSWS {OKTA_API_TOKEN}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def create_user(profile):
    """
    Creates a new Okta user in a deprovisioned state.
    """
    url = f"{OKTA_DOMAIN}/api/v1/users?activate=false"
    body = {
        "profile": profile,
        "credentials": {
            "password": {"value": "TempPassword123!"}
        }
    }

    response = requests.post(url, json=body, headers=headers)

    if response.status_code == 200:
        user_id = response.json()['id']
        print(f"✅ Created user: {user_id}")
        return user_id
    else:
        print(f"❌ Failed to create user: {response.text}")
        return None

def activate_user(user_id):
    """
    Activates a previously created user.
    """
    url = f"{OKTA_DOMAIN}/api/v1/users/{user_id}/lifecycle/activate?sendEmail=true"
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ Activated user: {user_id}")
    else:
        print(f"❌ Failed to activate user: {response.text}")

def assign_user_to_group(user_id, group_id):
    """
    Assigns a user to a group.
    """
    url = f"{OKTA_DOMAIN}/api/v1/groups/{group_id}/users/{user_id}"
    response = requests.put(url, headers=headers)

    if response.status_code == 204:
        print(f"✅ Assigned user to group: {group_id}")
    else:
        print(f"❌ Failed to assign to group: {response.text}")

def deactivate_user(user_id):
    """
    Deactivates a user.
    """
    url = f"{OKTA_DOMAIN}/api/v1/users/{user_id}/lifecycle/deactivate"
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print(f"✅ Deactivated user: {user_id}")
    else:
        print(f"❌ Failed to deactivate user: {response.text}")
