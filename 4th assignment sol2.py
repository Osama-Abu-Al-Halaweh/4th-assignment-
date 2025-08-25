price={"banana" : 15,"apple" :19,"orange" :29, "lemone" : 10, "mango" : 25 , "water melone" : 7}
x=input("enter fruit name please :").lower()
cost = price.get(x)

if cost is not None:
    print(f"{x} price is :",price[x])
else:
    print(f"{x} is not exist sorry!")