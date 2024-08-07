
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
lower_bound = 2
upper_bound = 6

count = 0
total_sum = 0

if lower_bound > upper_bound:
    print (f'The interval [{lower_bound}, {upper_bound}] does not exist. '
           'The lower bound must be less than the upper bound. '
           'They must be swapped.'      
    )
    lower_bound, upper_bound = upper_bound, lower_bound

for number in numbers:
        if lower_bound <= number <= upper_bound:
            count += 1
            total_sum += number
print(f'Amount of integers from the list {numbers} '
      f'in the interval [{lower_bound}, {upper_bound}] is {count}, '
      f'and their sum is {total_sum}.'    
)    
