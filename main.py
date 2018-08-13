#---------------------------------------------------------------------
# LCM and HCFs from Coding Challenges (HARD - solution)
# by Silvio Duka
#
# Last modified date: 2018-02-25
#
# LCM is the least common multiple of a set of numbers. 
# HCF is the highest common factor of a set of numbers. 
# 
# Consider 10 and 15: 
# Multiples of 10 are: 10, 20, 30, 40, ... 
# Multiples of 15 are: 15, 30, 45, 60, ... 
# => 30 is the LCM of 10 and 15. 
# 
# Factors of 10 are: 1, 2, 5, 10 
# Factors of 15 are: 1, 3, 5, 15 
# => 5 is the HCF of 10 and 15. 
#
# Tasks: 
# (Easy) Write a program to find the LCM and HCF of 2 numbers. 
# (Medium) Write a program to find the LCM and HCF of 3 numbers. 
# (Hard) Write a program to find the LCM and HCF of 4 or more numbers.
#---------------------------------------------------------------------

numbers = [10, 15] # Insert a list of N-numbers (minimum 2 numbers)

def lcm(numbers):
    numbers.sort()

    multipliedAll = 1
    for i in range(0, len(numbers)):
        multipliedAll *= numbers[i]

    for i in range(numbers[len(numbers)-1], multipliedAll + 1, numbers[len(numbers)-1]):
        t = 0
        for j in range(len(numbers)-1):
            t += i % numbers[j]
        if t == 0:
            return i
            
def hcf(numbers):
    numbers.sort()

    for i in range(numbers[0], 0, -1):
        t = 0
        for j in range(len(numbers)-1):
            t += numbers[j] % i
        if t == 0:
            return i

print("The LCM of [" + ",".join(str(n) for n in numbers) + "] is " + str(lcm(numbers)))
print("The HCF of [" + ",".join(str(n) for n in numbers) + "] is " + str(hcf(numbers)))