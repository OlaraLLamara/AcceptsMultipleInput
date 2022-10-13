# #Write a program which repeatedly reads numbers until the user enters "done". Once "done" is
# entered, print out the total, count, and average of the numbers. If the user enters anything other
# than a number, detect their mistake using try and except and print an error message and skip to
# the next number.

num = 0
total = 0.0
while True:
    number = input("Enter a number(enter the word done to terminate):  ")
    if number == 'done':
        break
    try :
        num1 = float(number)
    except:
        print('Invaid Input')
        continue
    num = num+1
    total = total + num1
print ('done encountered, terminated by user')
print("")
print("")
print('***************************************')
print ("The total is:", total)
print ("The Number of input accepted:", num)

if(num==0):
    print("cannot divide by zero")
else:
     print ("The average is:", total/num)

print ('**************************************')
print("")
print("")