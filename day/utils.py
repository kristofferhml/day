from datetime import datetime

def nanoseconds_to_hours(nanoseconds):
    # Convert nanoseconds to seconds
    seconds = nanoseconds / 1e9

    # Convert to a datetime object
    dt_object = datetime.utcfromtimestamp(seconds)

    # Extract the hour of the day
    hour_of_day = dt_object.hour

    return hour_of_day