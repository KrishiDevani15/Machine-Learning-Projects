def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2
# The ability for us to treat function as First-Class Object bascially means we can passed around as argument eg. int/string/float etc
def calculate(calc_function,n1,n2):
    return calc_function(n1,n2)

result = calculate(add,1,2)
print(result)

# Nested functions
def outer_function():
    print("I'M outer")
    
    def inner_function():
        print("I'M inner")

    inner_function()

outer_function()

# Function can be returned from other function
def first_function():
    print("I'M outer")
    
    def other_function():
        print("I'M inner")
        # other_function()
    return other_function

inner_function = first_function()
inner_function()
