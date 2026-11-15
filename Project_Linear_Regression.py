import sys as s

n=int(input("Enter the number of points :"))
x_values=[]
y_values=[]
xy_values=[]
x_squared_values=[]
for i in range(n):
    x=float(input(f"Enter the value of x{i+1} :"))
    x_values.append(x)

print("\n ================================================ \n")

for i in range(n):
    y=float(input(f"Enter the value of y{i+1} :"))
    # x_values.append(x)
    y_values.append(y)
    xy_values.append(x_values[i] * y_values[i])
    x_squared_values.append(x_values[i] ** 2)
x,y,xy,x_squared="x","y","xy","x^2"
print("-"*80)
print(x.center(20),y.center(20),xy.center(20),x_squared.center(20),"")
print("-"*80)

for i in range(n):
    x,y,xy,x_squared=str(x_values[i]),str(y_values[i]),str(f"{xy_values[i]:.5f}"),str(f"{x_squared_values[i]:.5f}")
    print(f" {x.center(18)}  {y.center(18)}   {xy.center(18)}      {x_squared.center(10)}")

sum_x=sum(x_values)
sum_y=sum(y_values)
sum_xy=sum(xy_values)
sum_x_squared=sum(x_squared_values)

print(f"\n Sum_x = {sum_x}, Sum_y = {sum_y}, Sum_xy = {sum_xy}, Sum_x^2 = {sum_x_squared}")

non_Zero=n*sum_x_squared-(sum_x)**2
if non_Zero==0:
    print("Error: Division by zero. The denominator is zero.")
    s.exit()

a1=(n*sum_xy-(sum_x*sum_y))/ non_Zero
a0=(sum_y)/n-a1*(sum_x/n)
print(f"\nEquation of the line: y = {a0:.4f} + {a1:.4f}x \n")
if a1>0:
    print("Positive Relationship \n ")
elif a1<0:
    print("Negative Relationship \n")

equ=input("you want to find y for a given x  yes or no :").strip().lower()

if equ=="yes":
    x=float(input("Enter the value of x :"))
    y=a0+a1*x
    print(f"The value of y for x={x} is {y:.4f}")      
    if  not  (min(x_values) <= x <=max(x_values)):

        print(" \n x is extrapolated because it is out of range")    

error=input("\n you want to find the Error( Min )   yes or no :")
Min=0
if error=="yes":
    predicted_y=[]
    for i in range(n):
       predicted_y.append(a0+a1*x_values[i]) 
       error=(predicted_y[i]-y_values[i])**2
       Min+=error

    print(f"The mean squared error Function is {Min:.8f}")   

