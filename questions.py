#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
    print("hello "+ user_name)

               
#Question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

#def first_odds():
for i in range(100):  
    if i % 2 !=0:
       print(i)
  
#Question 3
#Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
    print(max(a_list))

    max_num_in_list([-1,0,1,2,3]) 
             
#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
     
     if (a_year / 4) % 1 == 0:
        if (a_year / 100) % 1 != 0:
            return True
        elif (a_year / 400) % 1 == 0:
            return True
        else:
            return False
     else:
        return False

print(is_leap_year(1200))
               
#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
 min_num = min(a_list)
 max_num = max(a_list)

 if min_num == a_list[0] and max_num == a_list[len(a_list) - 1]:
        for item in a_list:
            n1 = item
            n2 = a_list[item - min_num]
            if item != max_num and n1 == n2:
                pass
            elif item == max_num:
                return True
            else:
                return False                
        else:
         return False

