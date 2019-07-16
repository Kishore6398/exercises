def leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return 1
            else:
                return 0
        else:
            return 1
yr=int(input("Enter a year"))
val=leap(yr)
if(val==1):
    print("Leap year")
else:
    print("Not a leap year")
            
        
        
