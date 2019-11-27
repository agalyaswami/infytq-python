def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    if(account_number[0]==1 and account_balance>=100000):
        if(salary>25000 and loan_type=="Car"):
            
            eligible_loan_amount=500000
            bank_emi_expected=36
        elif(salary>50000 and loan_type=="House"):
        
            eligible_loan_amount=6000000
            bank_emi_expected=60
        elif(salary>75000 and loan_type=="Business"):
            
            eligible_loan_amount=7500000
            bank_emi_expected=84
        else:
            print("invalid loan")
    else:
        print("invalid account number")
    

    
    print("Account number:", account_number)
    print("The customer can avail the amount of Rs.", eligible_loan_amount)
    print("Eligible EMIs :", bank_emi_expected)
    print("Requested loan amount:", loan_amount_expected)
    print("Requested EMI's:",customer_emi_expected)

calculate_loan(1001,40000,250000,"Car",300000,30)
  
    

