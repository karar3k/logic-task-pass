# Q2/Write a program to find all prime numbers up to a given range of numbers?

def is_prime(lower_value ,upper_value ):
    for number in range(lower_value,upper_value + 1):
        if number > 1:
            for i in range (2, number):  
                if (number % i) == 0:
                    break
            else:
                print("Is Prime : ", number)
is_prime(2,15)