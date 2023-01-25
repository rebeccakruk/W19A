def fizz_buzz(list):
    for num in nums:
        if (num % 3 == 0) and (num % 5 == 0):
            print('Fizz Buzz', num)
            continue
        elif (num % 3 == 0):
            print('Fizz', num)
            continue
        elif (num % 5 == 0):
            print('Buzz', num)
            
        
    

nums = [1,4,6,12,15,25,60,30,39,40,45,63,72,77,264,180,75,199,1560]
fizz_buzz(nums)