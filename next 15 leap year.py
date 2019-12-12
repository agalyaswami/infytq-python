def find_leap_years(given_year):
    count=0
    list_of_leap_years=[]
    while(count<15):
        if(given_year%4==0 and given_year%100!=0)or(given_year%400==0): 
            list_of_leap_years.append(given_year)
            count=count+1
            given_year=given_year+1
        else:
            given_year=given_year+1 
        
        

    return list_of_leap_years
