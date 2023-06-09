squared_minus_one = list() # This line initializes an empty list called squared_minus_one using the list() function. This list will be used to store the results of the calculations.
for n in range(1, 11):     #  This is a for loop that iterates over the numbers from 1 to 10 (inclusive). The loop variable n takes each value in this range one by one.  
    squared_minus_one.append((n ** 2) - 1) # In each iteration of the loop, this line calculates the square of the current value of n using the exponentiation operator **, and then subtracts 1 from the result. The calculated value is then appended to the squared_minus_one list using the append() method
    
    print(squared_minus_one)  # after the loop completes, this line prints the squared_minus_one list, which now contains the calculated values
    # [0, 3, 8, 15, 24, 35, 48, 63, 80, 99]