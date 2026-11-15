import sympy as sp
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

x=sp.symbols('x')
E=sp.E
In=sp.log
lower_in=sp.log
T=standard_transformations+(implicit_multiplication_application,convert_xor)
text=input("    Enter the equation : ")
#"sin(x)-e^-x
expr=parse_expr(text,local_dict={"x":x,"e":E,"In":In,"in":lower_in},transformations=T)
# print("The expression is : ",expr)

f=sp.lambdify(x,expr,"numpy")
dif=sp.diff(expr,x)
df=sp.lambdify(x,dif,"numpy")

x=float(input("K(0)    Enter the valua of x0 = "))
max_iterations = 200
accurate=10**-4
count=1
PRAE=0

while count<=max_iterations:
    if df(x)==0:
        print("    Error: Division by zero. The method cannot proceed.")        
        break
    x_next=x-(f(x)/df(x))
    if x_next==0:
        break
    PRAE= abs((x_next-x)/x_next)*100      # PRAE = percent Relative approximate error
    Approximate_Error=abs((x_next-x)/x_next)
    print(f"K({count})",end="")
    print(f"    the value of x{count } = {x_next:.8f}    precent Relative Approximate Error = {PRAE:.8f}%  f(x)={f(x_next):.8f}")
    count+=1
    if (Approximate_Error<accurate):
            break
    x=x_next     
else:
    print("Maximum iterations reached without convergence.")


