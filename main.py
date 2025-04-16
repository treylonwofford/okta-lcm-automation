# main.py

from config import OKTA_DOMAIN, OKTA_API_TOKEN
from utils import create_user, activate_user, assign_user_to_group, deactivate_user

# Replace these with dynamic input or CSV parsing if scaling
user_profile = {
    "firstName": "Jane",
    "lastName": "Doe",
    "email": "jane.doe@example.com",
    "login": "jane.doe@example.com"
}

group_id = "00gxxxxxxxxxxxxxxxxx"  # You can get this from Okta admin panel or API

if __name__ == "__main__":
    print("🚀 Starting Okta LCM Automation...")

    # 1. Create user
    user_id = create_user(user_profile)
    
    if user_id:
        # 2. Activate user
        activate_user(user_id)

        # 3. Assign to group
        assign_user_to_group(user_id, group_id)

        # 4. Optional: simulate deactivation
        deactivate_user(user_id)

    print("✅ Done.")
