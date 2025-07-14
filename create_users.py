import json
from django.contrib.auth import get_user_model
from phonenumber_field.phonenumber import PhoneNumber
from django_countries.fields import Country

# Get CustomUser model
CustomUser = get_user_model()

# Load JSON file
try:
    with open('users.json', 'r') as file:
        users_data = json.load(file)
except FileNotFoundError:
    print("Error: 'users.json' file not found. Please ensure the file exists in the current directory.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'users.json'. Please check the file syntax.")
    exit(1)

# Prepare CustomUser objects
users = []
for user_data in users_data:
    try:
        user = CustomUser(
            username=user_data['username'],
            email=user_data['email'],
            location=Country(user_data['location']),
            phone_number=PhoneNumber.from_string(user_data['phone_number'])
        )
        user.set_password(user_data['password'])  # Hash the password
        users.append(user)
    except KeyError as e:
        print(f"Error: Missing field {e} in user data: {user_data}")
        continue
    except ValueError as e:
        print(f"Error: Invalid data for user {user_data.get('username', 'unknown')}: {e}")
        continue
    except CustomUser.DoesNotExist:
        print(f"Error: Username {user_data['username']} already exists.")
        continue

# Bulk create
if users:
    try:
        CustomUser.objects.bulk_create(users)
        print(f"Successfully created {len(users)} users!")
    except Exception as e:
        print(f"Error during bulk_create: {e}")
else:
    print("No users created. Check your JSON data for errors.")