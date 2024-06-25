#q1
num=int(input("enter a number:"))
count=0
while num>0:
    num=int(num/10)
    count+=1
print("the count is :",count)

#q2
try:
    n=input("enter a number:")
    n=int(n)
    fact=1
    for i in range(1,n+1,1):
     fact*=i
    print("factorial is:",fact)

except ValueError:
    print("invalid input")

#q3
Computers ={
  "Laptop1" : {"brand" : "DELL","OS" : "Windows"},
  "Laptop2" : {"brand" : "HP", "OS" : "Linux"},
  "Desktop" : {"brand" : "Apple","OS" : "Mac-OS"}
}
brand=[Computers["Laptop1"]["brand"],Computers["Laptop2"]["brand"],Computers["Desktop"]["brand"]]
OS=[Computers["Laptop1"]["OS"],Computers["Laptop2"]["OS"],Computers["Desktop"]["OS"]]
print(brand)
print(OS)

