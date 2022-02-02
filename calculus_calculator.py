print("Hello, This is a Calculus Calculator Created by Adekolu Samuel(Samix Yasuke) ")
input01 = int(input("""What Operation Would You Like To Perform?
1. Simple Differentiation :  
2. Simple Integration : """))

if (input01 == 1):
    print("This is a simple differentiation calculator")
    # The above code is a code to display a text
    x_coefficient = int(input("Enter the coefficient of x: "))
    # The above code allows users to input the coefficient of x
    power = int(input("Enter the power of x: "))
    # The above code allows users to input the power of x
    print('y = '+str(x_coefficient)+'x'+'^'+str(power))
    # The above code displays a line of text in the form y=nx^n where n is a variable
    a = (x_coefficient*power)
    # The above code multiplies the coefficient of x by the power of x
    b = (power-1)
    # The above code subtracts the power of x by 1
    print("dy/dx= "+str(a)+'x'+'^'+str(b))
    # The above code displays the final answer which is in the form dy/dx=nxn^-1

if (input01 == 2):
    from fractions import Fraction
    coefficient_of_x = int(input("Input The Coefficient Of X: "))
    power_of_x = int(input("Input The Power Of X: "))
    print("dy= "+str(coefficient_of_x)+"x^"+str(power_of_x))
    sum_of_power = (power_of_x + power_of_x)
    sum_of_power_2 = (power_of_x + power_of_x)
    dif = (coefficient_of_x / sum_of_power_2)
    print("y="+str(Fraction(dif))+"x^"+ str(sum_of_power))