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

#q4
def Listinput(n):
  list=[]
  print("Enter elements of list")
  for i in range (0,n,1):
   a=int(input())
   if a%2==0:
      list.append(a)
  return list
n=int(input("Enter lenght of list:"))
print(Listinput(n))

#q5
def strings(str):
    l=len(str)
    vow=0
    con=0
    space=0
    for i in range (0,l,1):
        if((str[i]>='a' and str[i]<='z') or (str[i]>='A' and str[i]<='Z')):
         if (str[i]=='a'or str[i]=='e'or str[i]=='i'or str[i]=='o'or str[i]=='u'or str[i]=='A'or str[i]=='E'or str[i]=='I'or str[i]=='O'or str[i]=='U'):
             vow+=1
         else:
             con+=1   
    print("vowels:",vow,"consonants", con)
str=input("Enter a string")
strings(str) 

#q6
def Strings():
   n=int(input("enter lenght of list"))    
   str=[]
   print("Enter elements of list")
   for i in range (0,n,1):
    a=input()
    str.append(a)
   long=0
   largest=""
   for i in range(0,n,1):
     word=str[i]
     l=len(word)
     if(long<l):
         long=l
         largest=word
        
   print("Largest String is:",largest,"with lenght:",long)

Strings()

