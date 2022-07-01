# 1 package <= 20 kg
# 1 element range 1, 10 kg (end if smaller, bigger or not 0)

# 1. how many packages sent
# 2. how many kg sent
# 3. not used space (how many packages * 20 - kg sent)
# 4. which had most not used space

import sys

tpl = 'Packages sent: {}\nPackages total weight: {} [kg]\nUnused space: {} [kg]\nMost unused space: {} [kg]\n'

current_elements_weight = int()
package_counter = int()
package_weight_counter = int()
most_weight_difference = int()
weight_difference = int()
total_unused_space = int()
filename = input()

with open(filename) as file:
    for element_weight in file:
        element_weight = int(element_weight)
        if 1 < element_weight <= 10:
            current_elements_weight += element_weight
            if current_elements_weight > 20:
                current_elements_weight -= element_weight
                weight_difference = 20 - current_elements_weight
                if weight_difference > most_weight_difference:
                    most_weight_difference = weight_difference
                package_weight_counter += current_elements_weight
                package_counter += 1
                total_unused_space = package_counter * 20 - package_weight_counter
                current_elements_weight = element_weight
                print(tpl.format(package_counter, package_weight_counter, total_unused_space, most_weight_difference))
        else:
            print('Wrong value provided! You broke the program!')
            break