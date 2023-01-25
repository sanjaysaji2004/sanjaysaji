
a=int(input("Enter the number of elements: "))
b=[]
if(a>0):
    for i in range(0,a):
        c=int(input("Enter the elements: "))
        b.append(c)
    print("The List of elements : ",b)
    def sumsquare(b):
        odd=0
        even=0
        for i in b:
            if i%2==0:
                even = even+i**2
            else:
                odd=odd+i**2
                b=[odd,even]
        return(b)
    print(sumsquare(b))
else:
    print("Number of elements should be greater than zero")






















