def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    if legs%2==0:#legs must be even multiples
        rabbit_count = (legs//2) - heads
        chicken_count = heads - rabbit_count
    
        if rabbit_count<0 or chicken_count<0:
            print(error_msg)
        else:
            print(chicken_count,rabbit_count)
    else:
        print(error_msg)
solve(38,131)
