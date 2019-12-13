def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number-1)



def find_strong_numbers(num_list):
     strongNumbersList = []
     for item in num_list:
         currentNumber = item
         digits = []
         while currentNumber > 0:
            digits.insert(0, currentNumber % 10)
            currentNumber = currentNumber // 10
         if sum(map(factorial, digits)) == item:
             strongNumbersList.append(item)
     return strongNumbersList




num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
