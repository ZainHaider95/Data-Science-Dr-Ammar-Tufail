'''
# Loop 1: While

x=0
while (x<=5):
    print(x)
    x=x+1



# Loop 2: For

for x in range (5,10):
    print(x)  # The data in range will be printed.



# Working with Arrays

days= ['Mon','Tues','Wed','Thu','Fri','Sat','Sun'] 

for d in days:
    print (d)


# Using break in Array

days= ['Mon','Tues','Wed','Thu','Fri','Sat','Sun'] 

for d in days:
    if d == 'Fri':
        break        # break means stoping the loop
    print (d)



# Using continue in Array

days= ['Mon','Tues','Wed','Thu','Fri','Sat','Sun'] 

for d in days:
    if d == 'Fri':
        continue        # continue means skiping value in the loop
    print (d)

'''
# Using pass in Array

days= ['Mon','Tues','Wed','Thu','Fri','Sat','Sun'] 

for d in days:
    if d == 'Fri':
        pass        # pass means to do nothing in the loop
    print (d)

