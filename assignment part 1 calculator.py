print("-----------------------------\n"
      "------assignment part 1------\n"
      "-----------------------------\n")

print("A simple calculator that perform arithmatic operations regardless of their index position.")

option=input("Enter an arithmetic operation:") # step 1 : Ask user to enter input
print(option)
option= option.replace(" ", "")  #step 2 remove spaces
w=option.split('+') # step 3 indentify a and b regardless their position
x= option.split('-')  
y=option.split('*')
z=option.split('/')
    
if "+" in option: #check for + sign
    a = int(w[0])
    b = int(w[1])

    result = a + b
    print("The result is = " + str(result))
        
elif "*" in option: #check for * sign
    a = int(y[0])
    b = int(y[1])

    result = a * b
    print("The result is = " + str(result))
    
elif "/" in option: #check for / sign
    a= int(z[0])
    b= int(z[1])
    result = a / b
    result =round(result,3)
    print("The result is = " + str(result))    
    
    
elif "--" in option and len(x)==3:  #check for - sign and a is positve
    a= int(x[0])
    b= int(x[2])  
    result = a -- b
    print("The result is = ", result)
        
elif "-" in option and len(x) == 3: #check for - sign and a is negative
    a = int(x[1])
    b = int(x[2])
    result = a + b
    result = result * (-1)
    print("The result is = ", result)

elif "-" in option and len(x)==2:  #check for - sign and a is positve
    a= int(x[0])
    b= int(x[1])  
    result = a - b
    print("The result is = ", result)
        
elif "-" in option and len(x) == 4: 
    a = int(x[1])
    b = int(x[3])

    result = -a -- b
    print("The result is = ", result)
else:
    count = 3


