import json
from django.contrib.auth import get_user_model  # Replace 'myapp' with your app name
from trips.models import Trip
from datetime import datetime

# Get CustomUser model
CustomUser = get_user_model()

# Load JSON file
try:
    with open('trips.json', 'r') as file:
        trips_data = json.load(file)
except FileNotFoundError:
    print("Error: 'trips.json' file not found. Please ensure the file exists in the current directory.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'trips.json'. Please check the file syntax.")
    exit(1)

# Prepare Trip objects
trips = []
for trip_data in trips_data:
    try:
        # Validate user_id
        user = CustomUser.objects.get(id=trip_data['user_id'])

        # Validate dates
        start_date = datetime.strptime(trip_data['start_date'], '%Y-%m-%d').date()
        end_date = datetime.strptime(trip_data['end_date'], '%Y-%m-%d').date()
        if end_date < start_date:
            raise ValueError("end_date cannot be before start_date")

        trip = Trip(
            user=user,
            title=trip_data['title'],
            destination=trip_data['destination'],
            start_date=start_date,
            end_date=end_date,
            description=trip_data['description'],
            cover_photo=trip_data['cover_photo'],  # Set to None if null
            is_public=trip_data['is_public']
        )
        trips.append(trip)
    except KeyError as e:
        print(f"Error: Missing field {e} in trip data: {trip_data}")
        continue
    except CustomUser.DoesNotExist:
        print(f"Error: User ID {trip_data.get('user_id', 'unknown')} does not exist.")
        continue
    except ValueError as e:
        print(f"Error: Invalid data for trip {trip_data.get('title', 'unknown')}: {e}")
        continue
    except Exception as e:
        print(f"Error: Issue with trip {trip_data.get('title', 'unknown')}: {e}")
        continue

# Bulk create
if trips:
    try:
        Trip.objects.bulk_create(trips)
        print(f"Successfully created {len(trips)} trips!")
    except Exception as e:
        print(f"Error during bulk_create: {e}")
else:
    print("No trips created. Check your JSON data for errors.")