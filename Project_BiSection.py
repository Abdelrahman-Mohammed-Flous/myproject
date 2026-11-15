import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

x=sp.symbols('x')
E=sp.E
T=standard_transformations+(implicit_multiplication_application,convert_xor)
text=(input("Enter the equation : ")).center(5)
#"sin(x)-e^-x
expr=parse_expr(text,local_dict={"x":x,"e":E},transformations=T)
# print("The expression is : ",expr)

f=sp.lambdify(x,expr,"numpy")

x_previos= float((input("Enter the value of xu: ")).center(5))
x_current = float((input("Enter the value of xl: \n")).center(5))
accurate = 10**-4
PRAE = 0
count=2
max_iterations = 200


if f(x_current) * f(x_previos) > 0:
    print("This equation does not have a solution or have many solutions")
else:
    while abs(x_current - x_previos) != 0 and count-2 <= max_iterations:
        Xr= (x_current + x_previos) / 2
        Approximate_Error = abs(x_current - x_previos)

        if x_current != 0:
            PRAE = abs((x_current - x_previos) / x_current) * 100  # PRAE = percent Relative approximate error

        i=count-2
        
        if accurate >= Approximate_Error:
           
            print( f"k ({str(i).zfill(3)})  Xl = {str(x_current).center(17)}      Xu = {str(x_previos).center(17)}      Xr = {str(Xr).center(17)}  percent Relative approximate error = {PRAE:.8f}%")
                      
            # print( f"k ({str(i).zfill(3)})  Xl = {str(x_current).center(17):.12s}      Xu = {str(x_previos).center(17):.12s}      Xr = {str(Xr).center(17):.12s}      percent Relative approximate error = {PRAE:.8f}%")
            
            
            break

        if f(x_previos) * f(Xr) < 0:
            x_current = Xr
        else:
            x_previos = Xr

      
      
        # print( f"k ({str(i).zfill(3)})  Xl = {str(x_current).center(17):.12s}      Xu = {str(x_previos).center(17):.12s}      Xr = {str(Xr).center(17):.12s}      percent Relative approximate error = {PRAE:.8f}%")
       
        print( f"k ({str(i).zfill(3)})  Xl = {str(x_current).center(17)}      Xu = {str(x_previos).center(17)}      Xr = {str(Xr).center(17)}  percent Relative approximate error = {PRAE:.8f}%")
                    
        count+=1