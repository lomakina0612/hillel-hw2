
numbers = [-1, 2, 3, 4, 5, 6, 7, 8, -9]
lower_bound = 2
upper_bound = 8

count = 0
total_sum = 0

if lower_bound > upper_bound:
    print ('The lower bound must be less than the upper bound.'
           f'The interval [{lower_bound}, {upper_bound}] does not exist'
    )
else: 
    for number in numbers:
        if number >= lower_bound and number <= upper_bound:
            count += 1
            total_sum += number
    print(
        f'Amount of integers from the list {numbers} '
        f'in the interval [{lower_bound}, {upper_bound}] is {count}, '
        f'and their sum is {total_sum}'
    )
