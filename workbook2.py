###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

# My code
# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#     # YOUR CODE HERE
#     if day < 30:
#         day += 1
#     else:
#         day = 1
#         if month < 12:
#             month += 1
#         else:
#             month = 1
#             year += 1
#     return year, month, day
# # Udacity Solution
# def nextDay(year, month, day):
#     """
#     Returns the year, month, day of the next day.
#     Simple version: assume every month has 30 days.
#     """
#     # YOUR CODE HERE
#     if day < 30:
#         return year, month, day + 1
#     else:
#         if month < 12:
#             return year, month + 1, 1
#         else:
#             return year + 1, 1, 1

# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
def sameDay(year1, month1, day1, year2, month2, day2):
    if (year1 == year2) and (month1 == month2) and (day1 == day2):
        return True
    else:
        return False
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    daycount = 0
    while not sameDay(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        daycount += 1
    return daycount

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:" +args+ "failed")
        else:
            print("Test case passed!")

test()

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    if (year1 != year2) and (month1 != month2) and (day1 != day2):
        raise AssertionError
    return False        
