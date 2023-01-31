#sumsquare
a=[2,3,4,5,6,7,8,9,10]
def sumsquare(a):
    even = 0
    odd = 0
    for i in a:
        if i % 2 == 0:
            even += i**2
        else:
            odd += i**2
    return [even, odd]
print("output: ",sumsquare(a))
