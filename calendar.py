# A simple Python program to print a calendar of a given month and year

# Main function to print the whole month (title + body)
def printmonth(year, month):
    printmonthtitle(year, month)
    printmonthBody(year, month)

# Function to print the title/header of the calendar
def printmonthtitle(year, month):
        print("     ", getmonthname(month), " ", year)  # Print month name and year
        print("----------------------------------")       # Decorative line
        print("SUN   MON   TUE   WED   THU   FRI   SAT")  # Days of the week with equal spacing

# Function to print all the dates in proper positions
def printmonthBody(year, month):
    startday = getstartday(year, month)                  # Find which day the month starts on
    NumberOfDaysInmonth = gettotalNumberOfDaysInMonth(year, month)  # Total days in the month

    # Print empty slots before the first day of the month
    for i in range(0, startday):
        print("     ", end='')  # 5 spaces per empty slot for alignment

    # Print each day of the month
    for i in range(1, NumberOfDaysInmonth + 1):
        print(format(i, '5d'), end='')  # Each date takes 5 spaces (aligned cells)

        # Move to next line every 7 days (after Saturday)
        if (i + startday) % 7 == 0:
            print()

# Function to get month name from number
def getmonthname(month):
    Names = ["January", "February", "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]
    return Names[month-1]   # List index starts from 0, so use month-1

# Function to calculate which day the month starts (0=Sunday, 1=Monday, etc.)
def getstartday(year, month):
    START_DAY_FOR_JAN_1_1700 = 3    # Known fixed value: Jan 1, 1700 was a Wednesday (3)
    totalNumberOfDays = getTotalNumberOfDays(year, month)  # Count total days passed since 1700
    return (totalNumberOfDays + START_DAY_FOR_JAN_1_1700) % 7  # Use modulo to get weekday

# Function to count total days from 1700 up to the given year and month
def getTotalNumberOfDays(year, month):
    total = 0

    # Add total days for all full years from 1700 to the given year
    for i in range(1700, year):
        if isleapyear(i):
            total += 366
        else:
            total += 365

    # Add total days for all months before the given month in the same year
    for i in range(1, month):
        total += gettotalNumberOfDaysInMonth(year, i)

    return total

# Function to get number of days in a specific month of a given year
def gettotalNumberOfDaysInMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31             # Months with 31 days
    if month in [4, 6, 9, 11]:
        return 30             # Months with 30 days
    if month == 2:
        return 29 if isleapyear(year) else 28  # February logic (leap year or not)
    return 0

# Function to check if a year is a leap year
def isleapyear(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

# Main program input and execution
def main():
    year = int(input("Enter the year (e.g., 2020): "))
    month = int(input("Enter the month number (1-12): "))
    printmonth(year, month)

main()

