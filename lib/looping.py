#!/usr/bin/env python3

def happy_new_year():
    # code goes here
    i = 10
    while( i > 0):
        print(i)
        i -= 1
        if(i == 0):
            print("Happy New Year!")
    pass

def square_integers(int_list):
    for num in int_list:
        print(num ** 2)
        return [num **2 for num in int_list]
        
    # code goes here!
    
    pass

def fizzbuzz():
    # code goes here!
    i = 0
    while (i < 100):
        i += 1
        if (i % 3 == 0 and i % 5 ==0):
             print("FizzBuzz")
        elif(i % 3 == 0):
             print("Fizz")
        elif(i % 5 == 0):
             print("Buzz")
        else:
             print(i)
    pass
