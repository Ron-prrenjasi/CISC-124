import math
def main():
    while True: 
        x = input("Enter the first number \n or '0' to quit : ")
        if (x == '0'):
            break
        else:
            oper = input("Enter operation : ")
            if (oper == '+' or oper == '-'
             or oper == '*' or oper == '/'
             or oper == 'e'):
                   y = input("Enter the second number : ")
                
            if (oper == '+'):
                print(int(x) + int(y),'\n')
            elif (oper == '-'):
                print(int(x) - int(y),'\n')
            elif (oper == '*'):
                print(int(x) * int(y),'\n')
            elif (oper == '/'):
                print(int(x) / int(y),'\n')
            elif (oper == 'e'):
                if (int(y) >= 0 and isinstance(int(y), int)):
                    i=0
                    exp = 1
                    while (i < int(y)):
                        exp = exp * int(x)
                        i += 1
                    print(exp,'\n')
                else:        
                    print("error: illegal exponent\n")
            elif (oper == 's'):
                if (int(x) > 0):
                    print(math.sqrt(int(x)),'\n')
                else:
                    print("error: negative squre root\n")
            else:
                print("error: unknown operation\n")

main()    
