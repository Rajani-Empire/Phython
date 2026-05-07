num = int(input("Enter a number : "))


if num%2==0:
    print("number is even")
    
else:
    print("number is odd")


indian = ["somocha","dal","naan"]
chinese = ["egg role","pot sticker","fried rice"]
italian = ["pizza","pasta","risotto"]

dish = input("Enter a dish name : ")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("another country food")

num1 = int(input("Enter a number : "))


if num1%2==0 and num1>10:
    print("number is even")
    
else:
    print("number is odd")
