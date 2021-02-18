# Import the datetime.datetime module
from datetime import datetime, timedelta

# Get today's date and day
date = datetime.now().date()  # + timedelta(days=3)
day = date.strftime("%a")

# Check for fare
if day == "Mon" or day == "Tue" or day == "Wed" or day == "Thu" or day == "Fri":
    fare = 100
elif day == "Sat":
    fare = 60
elif day == "Sun":
    fare = 80
else:
    fare = None

# Print results
print("Date:\t", date)
print("Day:\t", day)
print("Fare:\t", fare)