import datetime as dt
import time

print("=" * 50)
print("🎂 WELCOME TO YOUR BIRTHDAY COUNTDOWN 🎂")
print("=" * 50)


attempts = 0

while attempts < 3:
    try:
        dob = input("\nEnter your date of birth (YYYY/MM/DD): ")

        parts = dob.split("/")

        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])

        date_birth = dt.datetime(year, month, day)

        if date_birth > dt.datetime.now():
            print("❌ Birth date cannot be in the future.")
            attempts += 1
            continue

        break

    except (ValueError, IndexError):
        print("❌ Invalid date format. Please use YYYY/MM/DD.")
        attempts += 1

if attempts == 3:
    print("\nToo many invalid attempts. Goodbye!")
    quit()



today = dt.date.today()

age = today.year - year

if (today.month, today.day) < (month, day):
    age -= 1

print(f"\n🎉 You are currently {age} years old.")



weekday_names = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]

weekday_num = date_birth.weekday()

print("\nYou may have forgotten which day of the week you were born on...")
print("🗓️ You were born on a", weekday_names[weekday_num])



print("\n📅 Weekdays of all your birthdays:")

for y in range(year, today.year + 1):
    try:
        bday = dt.datetime(y, month, day)
        print(y, "-", weekday_names[bday.weekday()])

    except ValueError:
        # Skip invalid leap-year dates
        pass



current_time = dt.datetime.now()
thisyear = current_time.year

try:
    thisyear_bday = dt.datetime(thisyear, month, day)

except ValueError:
    # Handles 29 Feb birthdays
    thisyear_bday = dt.datetime(thisyear, 2, 28)

if thisyear_bday > current_time:
    next_bday = thisyear_bday
else:

    try:
        next_bday = dt.datetime(thisyear + 1, month, day)

    except ValueError:
        next_bday = dt.datetime(thisyear + 1, 2, 28)

print("\n🎂 Your next birthday will be on:")
print(next_bday.strftime("%d %B %Y"))

weekday_num = next_bday.weekday()

print("🗓️ That will be a", weekday_names[weekday_num])



def get_time_left(next_bday):
    current_time = dt.datetime.now()

    dd = next_bday - current_time

    days_left = dd.days

    # Convert to string and use split()
    time_string = str(dd)

    if ":" in time_string:
        parts = time_string.split(":")

        hours = int(parts[0].split()[-1])
        minutes = int(parts[1])
        seconds = int(parts[2].split(".")[0])

    else:
        hours = 0
        minutes = 0
        seconds = 0

    return days_left, hours, minutes, seconds


input("\nPress ENTER to start the live countdown...")

while next_bday > dt.datetime.now():

    days_left, hours, minutes, seconds = get_time_left(next_bday)

    print(
        f"\r🎂 {days_left}d {hours:02d}h {minutes:02d}m {seconds:02d}s until your birthday!     ",
        end="",
        flush=True
    )

    time.sleep(1)


print("\n\n🎉🎉 HAPPY BIRTHDAY! 🎉🎉")
print("🥳 Have an amazing day!")
