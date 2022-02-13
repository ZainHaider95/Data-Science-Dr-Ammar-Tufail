'''

# Defining Function Methord: 1

def code():
    print(" We are Learning Python")
    print(" We are Learning Python")

code() # calling function

# Defining Function Methord: 2

def code():
    text= " We are Learning Python"
    print(text)
    print(text)

code() # calling function


# Defining Function Methord: 3

def code(text):
   
    print(text)
    print(text)

code(" We are Learning Python") # calling function


# Defining School Age Calculation Using Function and if,else,elif Statements

def school_calculation(age):

    if age == 5:
        print("The Kid can go to school.")
    elif age > 5:
        print("The Kid should go to higher class.")
    else:
        print ("The Kid is still a baby.")

school_calculation(7)

'''

# Finding future age 

def FutureAge (age):
    NewAge= age + 20
    return (NewAge)

FuturePredictedAge = FutureAge (25)
print(FuturePredictedAge)

