print("-----------------------------\n"
      "------Assignment part 2------\n"
      "-----------------------------\n")
print("===You have 3 tries===\n"
      "------Be careful------")

print("Iftiaj Alom")
print("1001956795")

import sys

count = 0


while count <3: #count number of tries
    option = input("Enter an Arithmethic Operation: ")
    print(option)
    
#check for invalid Operations

    if "++" in option:
        print("Invalid Arithmethic Operation. Please try again.") 
        count += 1
        continue
    elif "--" in option and "+" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1
        continue
    elif "--" in option and "*" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1
        continue
    elif "--" in option and "/" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1
        continue
    elif "**" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1  
        continue
    elif "//" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1 
        continue

    elif "+*" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1  
        continue
    elif "+/" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1  
        continue
    elif "-/" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1     
        continue
    elif "*/" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1   
        continue
    elif "-+" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "/*" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1   
        continue
    elif "a" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "b" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "ab" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "k" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "z" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "x" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "c" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "v" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "s" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "d" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "f" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "h" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "j" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "q" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "w" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "e" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "r" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "t" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "y" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "u" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "i" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "o" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "p" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "l" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "n" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    elif "m" in option:
        print("Invalid Arithmethic Operation. Please try again.")
        count += 1    
        continue
    else:
        break
if count == 3:
    print(" Your 3 tries are over. The program Terminated.")
    sys.exit()
else:
    pass
    
    option= option.replace(" ", "")  # remove spaces
    w=option.split('+') # indentify a and b regardless their position
    x= option.split('-')  
    y=option.split('*')
    z=option.split('/')
    
    if "+" in option: #check for + Operation
        a = int(w[0])
        b = int(w[1])

        result = a + b
        print("The result is = " + str(result))
        
    elif "*" in option: #check for * Operation
        a = int(y[0])
        b = int(y[1])

        result = a * b
        print("The result is = " + str(result))
    
    elif "/" in option: #check for / Operation
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