# Import the datatime module
import datetime

# Get the current data and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Get the current date
current_date = now.date()
print(f"Current Date: {current_date}")

# Get the current time
current_time = now.time()
print(f"Current Time: {current_time}")

# Formatting the date and time
formatted_date = now.strftime("%d-%m-%Y")
formatted_time = now.strftime("%H:%M:%S")
print(f"Formatted date: {formatted_date}")
print(f"Formatted time: {formatted_time}")

# Create a specific date
specific_date = datetime.datetime(2024,10,3)
print(f"Specific date: {specific_date}")

# Adding 10 days to the current date
future_date = current_date + datetime.timedelta(year = 10)
print(f"Date after 10 days: {future_date}")

# Subtracting 5 days to the current date
past_date = current_date - datetime.timedelta(days = 5)
print(f"Date 5 days ago: {past_date}")
