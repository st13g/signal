import random
from datetime import datetime

def get_value_from_file(filename, offset):
    # Open the file for reading
    with open(filename, 'r') as f:
        # Read the stored value as an integer
        stored_value = int(f.read())

    # Check if the stored value is zero
    if stored_value == 0:
        # Return 0 if the stored value is zero
        return 0

    # Get the current time
    now = datetime.now()

    # Check if the current time is between 7:00am and 8:00pm on Monday to Friday
    if now.weekday() < 5 and now.time() >= datetime.strptime('07:00:00', '%H:%M:%S').time() and now.time() <= datetime.strptime('20:00:00', '%H:%M:%S').time():
        # Generate a random number between -offset and +offset
        random_offset = random.randint(-offset, offset)

        # Add the random offset to the stored value
        new_value = stored_value + random_offset

        # Round the new value to the nearest integer
        new_value = round(new_value)

        # Return the new value as an integer
        return int(new_value)
    # Check if the current time is between 8:00am and 1:00pm on Saturdays
    elif now.weekday() == 5 and now.time() >= datetime.strptime('08:00:00', '%H:%M:%S').time() and now.time() <= datetime.strptime('13:00:00', '%H:%M:%S').time():
        # Generate a random number between -offset and +offset
        random_offset = random.randint(-offset, offset)

        # Add the random offset to the stored value
        new_value = stored_value + random_offset

        # Round the new value to the nearest integer
        new_value = round(new_value)

        # Return the new value as an integer
        return int(new_value)
    else:
        # Return 0 outside of the time ranges specified above or any time on Sundays
        return 0

value = get_value_from_file('value.txt', 2)
print(value)
