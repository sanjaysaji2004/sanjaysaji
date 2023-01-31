# Get number of loaves of day old bread from user
loaves = int(input("Enter number of loaves of day old bread: "))

# Calculate regular price
regular_price = loaves * 185

# Calculate discount
discount = regular_price * 0.6

# Calculate total price
total_price = regular_price - discount

# Display prices with two decimal places and aligned decimal points
print("Regular price:rupees",regular_price)
print("Discount:rupees",discount)
print("Total pricerupees",total_price)
