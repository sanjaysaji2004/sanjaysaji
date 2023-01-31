def max_guests(T, E, L):
    guests = 0
    max_guests = 0
    for i in range(T):
        guests += E[i] - L[i]
        max_guests = max(max_guests, guests)
    return max_guests

T = 5
E = [10, 20, 30, 40, 50]
L = [5, 10, 15, 20, 25]
print(max_guests(T, E, L))
