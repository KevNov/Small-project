#function for multiplying number

def multiply_num(nums):
    total = 1
    for val in nums:
        if val % 2 != 0:
            total = total * val
    return total

#print(multiply_num([1,2,3,4,5,6,7,8,9,10]))
#print(multiply_num(list(range(11,21))))

#function for summ all number

def sum_num(nums):
    return sum(num for num in nums if num % 2 == 0)
    #total = 0
    #for val in nums:
        #if val % 2 == 0:
            #total += val
    #return total

print(sum_num(list(range(20,41))))
print(sum_num(list(range(50,70))))

