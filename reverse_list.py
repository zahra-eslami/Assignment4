array_size=0
array=[]
i=1

try:
    array_size=int(input("please enter the size of your array : "))
except:
    print("You must enter an integer number:")

while array_size!= len(array):
    try:
        x=int(input(f"please enter your {i} number: "))
        array.append(x)
        i+=1
    except:
       print("please enter an integer number")

print("your array was : ", end="")
for i in array:
    print(i,end = " ")

array.reverse()
print("\n your new array is: ",end="")

for i in array:
    print(i,end=" ")