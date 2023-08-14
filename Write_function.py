def is_leap(year):
    leap = False
    
    if ((year % 400 == 0) and (year % 100 == 0)) | ((year % 4 ==0) and (year % 100 != 0)):
        
        # change leap to True
         leap = True
    return leap

year = int(input())
print(is_leap(year))