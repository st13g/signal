import random
from datetime import datetime



def get_value_from_file(filename, offset):
    # Get the current time
    now = datetime.now().time()

    # Check if the current time is between 7:00am and 8:00pm
    if now >= datetime.strptime('07:00:00', '%H:%M:%S').time() and now <= datetime.strptime('20:00:00', '%H:%M:%S').time():
        # Open the file for reading
        with open(filename, 'r') as f:
            # Read the stored value as an integer
            stored_value = int(f.read())

        # Generate a random number between -offset and +offset
        random_offset = random.randint(-offset, offset)

        # Add the random offset to the stored value
        new_value = stored_value + random_offset

        # Round the new value to the nearest integer
        new_value = round(new_value)

        # Return the new value as an integer
        return int(new_value)
    else:
        # Return 0 outside of the 7:00am to 8:00pm time range
        return 0
value = get_value_from_file('value.txt', 2)
print(value)
