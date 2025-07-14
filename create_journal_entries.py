import json
from datetime import datetime
from trips.models import Trip
from journals.models import JournalEntry

# Load JSON file
try:
    with open('journal_entries.json', 'r') as file:
        entries_data = json.load(file)
except FileNotFoundError:
    print("Error: 'journal_entries.json' file not found. Please ensure the file exists in the current directory.")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'journal_entries.json'. Please check the file syntax.")
    exit(1)

# Prepare JournalEntry objects
entries = []
for entry_data in entries_data:
    try:
        # Validate trip_id
        trip = Trip.objects.get(id=entry_data['trip_id'])

        # Validate entry_date
        entry_date = datetime.strptime(entry_data['entry_date'], '%Y-%m-%d').date()
        if not (trip.start_date <= entry_date <= trip.end_date):
            raise ValueError(
                f"entry_date ({entry_date}) must be between trip's start_date ({trip.start_date}) and end_date ({trip.end_date})")

        entry = JournalEntry(
            trip=trip,
            title=entry_data['title'],
            content=entry_data['content'],
            entry_date=entry_date
        )
        entries.append(entry)
    except KeyError as e:
        print(f"Error: Missing field {e} in entry data: {entry_data}")
        continue
    except Trip.DoesNotExist:
        print(f"Error: Trip ID {entry_data.get('trip_id', 'unknown')} does not exist.")
        continue
    except ValueError as e:
        print(f"Error: Invalid data for entry {entry_data.get('title', 'unknown')}: {e}")
        continue
    except Exception as e:
        print(f"Error: Issue with entry {entry_data.get('title', 'unknown')}: {e}")
        continue

# Bulk create
if entries:
    try:
        JournalEntry.objects.bulk_create(entries)
        print(f"Successfully created {len(entries)} journal entries!")
    except Exception as e:
        print(f"Error during bulk_create: {e}")
else:
    print("No journal entries created. Check your JSON data for errors.")