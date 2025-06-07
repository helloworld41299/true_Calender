def daynum(day, month, year):
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    return (year + year // 4 - year // 100 + year // 400 + t[month - 1] + day) % 7

def monthname(monthnum):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    if 0 <= monthnum < 12:
        return months[monthnum]
    return "Invalid"

def number_of_days(monthnum, year):
    if monthnum == 0:
        return 31
    if monthnum == 1:
        # February
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return 29
        else:
            return 28
    if monthnum in [2, 4, 6, 7, 9, 11]:
        return 31
    if monthnum in [3, 5, 8, 10]:
        return 30
    return 0

def print_calendar(year):
    print(f"Calendar - {year}\n")
    current = daynum(1, 1, year)

    for month in range(12):
        days = number_of_days(month, year)
        print(f"\n---------- {monthname(month)} ----------")
        print(" Sun Mon Tue Wed Thu Fri Sat")

        # Print leading spaces
        print("    " * current, end="")

        for day in range(1, days + 1):
            print(f"{day:4}", end="")
            current += 1
            if current > 6:
                current = 0
                print()
        if current != 0:
            print()  # Newline at the end of the month

# Main Execution
if __name__ == "__main__":
    try:
        year = int(input("Enter year: "))
        print_calendar(year)
    except ValueError:
        print("Invalid input! Please enter a valid year.")
