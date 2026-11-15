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
text=input("    Enter the equation : ")
#"sin(x)-e^-x
expr=parse_expr(text,local_dict={"x":x,"e":E},transformations=T)
# print("The expression is : ",expr)

f=sp.lambdify(x,expr,"numpy")

x_previos=float(input("K(0)    Enter the valua of x0 = "))
Delta=float(input("    Enter the valua of  Delta = "))
x_current=x_previos+Delta
max_iterations = 200
accurate=10**-4
count=2
PRAE=0

while count<=max_iterations:
    non_Zero= f(x_current) - f(x_previos)
    if non_Zero==0:
        print("    Error: Division by zero. The method cannot proceed.")
        break
    x_next=x_current-((f(x_current)*(x_current-x_previos))/(non_Zero))
    if x_next==0:
         break
    PRAE= abs((x_next-x_previos)/x_next)*100      # PRAE = percent Relative approximate error
    Approximate_Error=abs((x_next-x_previos)/x_next)
    print(f"K({count})",end="")
    print(f"    the value of x{count } = {x_next:.8f}    precent Relative Approximate Error = {PRAE:.8f}%  f(x)={f(x_next):.8f}")
    count+=2
    if (Approximate_Error<accurate):
            break
    x_previos=x_next
    x_current=x_next+Delta   
else:
    print("Maximum iterations reached without convergence.")


