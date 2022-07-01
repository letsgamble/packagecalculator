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

current_elements_weight = int()

with open('in.txt') as file:
    for element_weight in file:
        if 1 < int(element_weight) <= 10:
            current_elements_weight += int(element_weight)
            print('Current total weight:', current_elements_weight)
        else:
            print('Wrong value provided! Program stopped.')
            break