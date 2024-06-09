def count_sundays(start_year, end_year):
    months_and_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    
    year_count = 1900
    month_count = 1
    weekday_tracker = 1
    
    sunday_count = 0
    
    while year_count <= end_year:
        if weekday_tracker == 7 and year_count >= start_year:
            sunday_count += 1
        
        days_forward = months_and_days[month_count]
        if month_count == 2 and (year_count % 100 != 0 and year_count % 4 == 0 or year_count % 400 == 0):
            days_forward = 29
        
        weekday_shift = days_forward % 7
        
        weekday_tracker += weekday_shift
        if weekday_tracker >= 8:
            weekday_tracker -= 7
        
        month_count += 1
        if month_count == 13:
            month_count = 1
            year_count += 1
        
    return sunday_count
           
year_start = 1901
year_end = 2000
print(count_sundays(year_start, year_end))       
    
    

#https://projecteuler.net/problem=19