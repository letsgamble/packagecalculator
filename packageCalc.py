# 1 package <= 20 kg
# 1 element range 1, 10 kg (end if smaller, bigger or not 0)

# 1. how many packages sent
# 2. how many kg sent
# 3. not used space (how many packages * 20 - kg sent)
# 4. which had most not used space

import sys
# current_element_weight = int()

# while True:
#     element_weight = int(input())
#     current_element_weight += element_weight
#     print('Element weight:', element_weight)
#     print('Total elements weight:', current_element_weight)

file_name = str(input('Please enter import file name: '))
element_weight = int()

with open(file_name) as file:
    for element_weight in file:
        print(element_weight, end='')
        if 'str' in element_weight:
            break