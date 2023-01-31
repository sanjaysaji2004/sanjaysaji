a=int(input("Enter the number :"))
def is_happy(n):
    def get_sum_of_squares(num):
        return sum([int(x)**2 for x in str(num)])

    seen = set()
    while n not in seen:
        seen.add(n)
        n = get_sum_of_squares(n)
        
    return n == 1

print("the number is happy or not(true/false): ",is_happy(a))














