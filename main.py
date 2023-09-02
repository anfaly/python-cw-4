def my_function():
    print ("My name is anfal")

my_function()

def my_meal(food, drink ):
    print (f"I like to eat {food} while drinking {drink}")

my_meal("Sandwitchs" , "Orange Juice")

def cube(number):
    return number**3

print (cube(3))

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False

print (by_three(9))