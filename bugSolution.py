def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Additional handling for non-numeric input
def calculate_average_robust(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num,(int,float))]
    if not numeric_numbers:
        return 0
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_mixed_list = [1,2,'a',4,5]
robust_average = calculate_average_robust(my_mixed_list)
print(f"The robust average is: {robust_average}")