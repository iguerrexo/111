print('Hello form Python')

last_name = 'Guerrero'
age = 20
found = False
total = 13.44

print(last_name)
print("Nora"+last_name)
print(age + age)

#this will give an error
print(last_name + str(age))
print (age + total)

#math
print('----------------------------------')
print(1 + 1)
print(42 - 21)
print(10 * 8)
print(101 - 3)
print(20 % 2)

#if
print('---------------------------------')
if(age < 99):
    print('You Are still Young')
    print('this is inside of the if')

print('this is outside of the if')


if(total > 100):
    print("you will get free shipping")
    print('')
elif(total > 50):
    print("pay half of the shipping")
else:
    print("you need to pay for shipping")


def say_hi():
            print('hi from a function')
            print('Still inside a function')

say_hi() # calling the fn
say_hi()